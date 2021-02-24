# t = int(input())
# for _ in range(t):
#     x , y , k , n = list(map(int,input().split()))

#     ## direction for thief
#     yl,yr = False , False
#     if y - k >=0 and n - y- k >=0:
#         yl = True if y < n - y  else False
#         yr = True if not yl else False
#     elif y - k >= 0:
#         yl = True 
#     elif n - y - k >=0:
#         yr = True 
#     ## direction for policeman
#     xl , xr = False , False
#     if x - k >=0 and n - x- k >=0:
#         xl = True if x < n - x  else False
#         xr = True if not xl else False
#     elif x - k >= 0:
#         xl = True 
#     elif n - x - k >=0:
#         xr = True 

#     stepsX,stepsY = [] , []
#     if xl:
#         while x >= k:
#             stepsX.append(x)
#             x -=k
#         while x <= n -k:
#             stepsX.append(x)
#             x += k 
#     elif xr:
#         while x <= n -k:
#             stepsX.append(x)
#             x += k 
#         while x >= k:
#             stepsX.append(x)
#             x -=k
#     if yl:
#         while y >= k:
#             stepsY.append(y)
#             y -= k
#         while y <= n - k:
#             stepsY.append(y)
#             y += k 
#     elif yr:
#         while y <= n - k:
#             stepsY.append(y)
#             y += k
#         while y >= k:
#             stepsY.append(y)
#             y -= k 
#     print(stepsX)
#     print(stepsY)
#     # flg = False
#     # for i in range(len(stepsY)):
#     #     if stepsY[i] == stepsX[i]:
#     #         flg = True
#     #         break
#     # if flg:
#     #     print("Yes")
#     # else:
#     #     print("No")
# def convert_examples_to_features(sentences, labels, max_seq_length, tokenizer):
#     """Loads a data file into a list of `InputBatch`s."""

#     input_ids, input_masks, segment_ids = [] , [] , []
#   # For every sentence...
#     for sent in sentences:
#       # `encode_plus` will:
#       #   (1) Tokenize the sentence.
#       #   (2) Prepend the `[CLS]` token to the start.
#       #   (3) Append the `[SEP]` token to the end.
#       #   (4) Map tokens to their IDs.
#       #   (5) Pad or truncate the sentence to `max_length`
#       #   (6) Create attention masks for [PAD] tokens.
#         encoded_dict = tokenizer.encode_plus(
#                           sent,                      # Sentence to encode.
#                           add_special_tokens = True, # Add '[CLS]' and '[SEP]'
#                           max_length = 64,           # Pad & truncate all sentences.
#                           pad_to_max_length = True,
#                           return_attention_mask = True,   # Construct attn. masks.
#                           return_token_type_ids=True,
#                           return_tensors = 'pt',     # Return pytorch tensors.
#                     )
      
#       # Add the encoded sentence to the list.    
#         input_ids.append(encoded_dict['input_ids'])
      
#       # And its attention mask (simply differentiates padding from non-padding).
#         input_masks.append(encoded_dict['attention_mask'])
#         segment_ids.append(encoded_dict['token_type_ids'])
    
#     return (
#         np.array(input_ids),
#         np.array(input_masks),
#         np.array(segment_ids),
#         np.array(labels)
#     )

def f1_score_func(preds, labels):
    preds_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()
    return f1_score(labels_flat, preds_flat, average='weighted')
def accuracy_per_class(preds, labels , label_dict):
    # label_dict_inverse = {v: k for k, v in label_dict.items()}
    
    preds_flat = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()

    for label in np.unique(labels_flat):
        y_preds = preds_flat[labels_flat==label]
        y_true = labels_flat[labels_flat==label]
        print(f'Class: {label_dict[label]}')
        print(f'Accuracy: {len(y_preds[y_preds==label])}/{len(y_true)}\n')

def evaluate(dataloader_val):
    
    model.eval()
    
    loss_val_total = 0
    predictions, true_vals = [], []
    
    for batch in dataloader_val:
        
        batch = tuple(b.to(device) for b in batch)
        
        inputs = {'input_ids':      batch[0],
                  'attention_mask': batch[1],
                  'labels':         batch[2],
                 }

        with torch.no_grad():        
            outputs = model(**inputs)
            
        loss = outputs[0]
        logits = outputs[1]
        loss_val_total += loss.item()

        logits = logits.detach().cpu().numpy()
        label_ids = inputs['labels'].cpu().numpy()
        predictions.append(logits)
        true_vals.append(label_ids)
    
    loss_val_avg = loss_val_total/len(dataloader_val) 
    
    predictions = np.concatenate(predictions, axis=0)
    true_vals = np.concatenate(true_vals, axis=0)
            
    return loss_val_avg, predictions, true_vals

for epoch in tqdm(range(1, epochs+1)):
    
    model.train()
    
    loss_train_total = 0

    progress_bar = tqdm(dataloader_train, desc='Epoch {:1d}'.format(epoch), leave=False, disable=False)
    for batch in progress_bar:

        model.zero_grad()
        
        batch = tuple(b.to(device) for b in batch)
        
        inputs = {'input_ids':      batch[0],
                  'attention_mask': batch[1],
                  'labels':         batch[2],
                 }       

        outputs = model(**inputs)
        
        loss = outputs[0]
        loss_train_total += loss.item()
        loss.backward()

        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

        optimizer.step()
        scheduler.step()
        
        progress_bar.set_postfix({'training_loss': '{:.3f}'.format(loss.item()/len(batch))})
         
        
    torch.save(model.state_dict(), f'finetuned_BERT_epoch_{epoch}.model')
        
    tqdm.write(f'\nEpoch {epoch}')
    
    loss_train_avg = loss_train_total/len(dataloader_train)             
    tqdm.write(f'Training loss: {loss_train_avg}')
    
    val_loss, predictions, true_vals = evaluate(dataloader_validation)
    val_f1 = f1_score_func(predictions, true_vals)
    tqdm.write(f'Validation loss: {val_loss}')
    tqdm.write(f'F1 Score (Weighted): {val_f1}')
