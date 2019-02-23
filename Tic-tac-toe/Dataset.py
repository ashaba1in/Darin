from Parse import white_data, black_data
import numpy as np
from copy import deepcopy
import torch
from torch import utils
import torch.utils.data

field_size = 15


# returns tensors of boards (1 - your stone, -1 - opponent's stone, 0 - empty cell)
# and labels (stone positions which are numbers from 0 to 224)
def create_dataset_white():
    data = []
    labels = []
    for game in white_data:
        board = [[0] * field_size for i in range(field_size)]
        is_black = True
        for turn in game:
            if is_black:
                board[turn[0] - 1][turn[1] - 1] = 1
            else:
                data.append(deepcopy(board))
                labels.append((turn[0] - 1) * 15 + turn[1] - 1)
                board[turn[0] - 1][turn[1] - 1] = -1

            is_black = not is_black

    x = [np.array(data[i]) for i in range(len(data))]
    data_x = torch.stack([torch.from_numpy(i).type(torch.FloatTensor) for i in x])

    y = [labels[i] for i in range(len(labels))]
    data_y = torch.stack([torch.tensor(i) for i in y])

    dataset = utils.data.TensorDataset(data_x, data_y)

    del data
    del labels
    del x
    del y
    del data_x
    del data_y
    return dataset


# returns tensors of boards (1 - your stone, -1 - opponent's stone, 0 - empty cell)
# and labels (stone positions which are numbers from 0 to 224)
def create_dataset_black():
    data = []
    labels = []
    for game in black_data:
        board = [[0] * field_size for i in range(field_size)]
        is_black = True
        for turn in game:
            if is_black:
                data.append(deepcopy(board))
                labels.append((turn[0] - 1) * 15 + turn[1] - 1)
                board[turn[0] - 1][turn[1] - 1] = 1
            else:
                board[turn[0] - 1][turn[1] - 1] = -1

            is_black = not is_black

    x = [np.array(data[i]) for i in range(len(data))]
    data_x = torch.stack([torch.from_numpy(i).type(torch.FloatTensor) for i in x])

    y = [labels[i] for i in range(len(labels))]
    data_y = torch.stack([torch.tensor(i) for i in y])

    dataset = utils.data.TensorDataset(data_x, data_y)

    del data
    del labels
    del x
    del y
    del data_x
    del data_y
    return dataset


data_w = create_dataset_white()
data_b = create_dataset_black()

white_train, white_test = torch.utils.data.random_split(data_w, (749207, 10000))
black_train, black_test = torch.utils.data.random_split(data_b, (809118, 10000))

del data_w
del data_b

batch_size = 50
white_train_loader = torch.utils.data.DataLoader(white_train, batch_size, shuffle=True)
white_test_loader = torch.utils.data.DataLoader(white_test, batch_size, shuffle=True)
black_train_loader = torch.utils.data.DataLoader(black_train, batch_size, shuffle=True)
black_test_loader = torch.utils.data.DataLoader(black_test, batch_size, shuffle=True)

del white_train
del white_test
del black_train
del black_test
