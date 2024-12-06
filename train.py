import os
import numpy as np
import torch
from torch.utils.data import DataLoader
from tacotron2_model import Tacotron2
from tacotron2_loss import Tacotron2Loss
from tacotron2_data import TextMelDataset, TextMelCollate

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyperparameters
batch_size = 32
epochs = 100
learning_rate = 1e-3

# Load dataset
dataset_path = '/path/to/your/dataset'
dataset = TextMelDataset(dataset_path)
collate_fn = TextMelCollate()
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=collate_fn)

# Initialize model
model = Tacotron2().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
criterion = Tacotron2Loss()

# Training loop
for epoch in range(epochs):
    model.train()
    epoch_loss = 0
    for batch in dataloader:
        inputs, targets = batch
        inputs, targets = inputs.to(device), targets.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        
        epoch_loss += loss.item()
    
    print(f'Epoch {epoch+1}/{epochs}, Loss: {epoch_loss/len(dataloader)}')

# Save the model
torch.save(model.state_dict(), 'tacotron2_model.pth')