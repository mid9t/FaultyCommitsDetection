from typing import Optional

import torch
from tqdm import trange, tqdm

from evaluation.offline_eval import eval_model
from evaluation.eval_structs import OperatingPointMetrics, EvalMetrics
from trainer.train_structs import TrainMetadata
from utils.utils import count_model_parameters


class ClassificationTrainer:
    """Class that trains a model on a given training dataset with a given criterion/optimizer.
    After each epoch, this runs the offline eval pipeline on the validation dataset, via `self.perform_validation()`.
    """
    def __init__(
            self,
            model: torch.nn.Module,
            criterion: torch.nn.Module,
            optimizer: torch.optim.Optimizer,
            train_data_loader: torch.utils.data.DataLoader,
            val_data_loader: Optional[torch.utils.data.DataLoader] = None,
            device: torch.device = torch.device("cpu"),
            log_every_n_batches: int = 20,
            skip_val: bool = False,
        ):
        """

        Args:
            model: Model to train.
            criterion: Criterion to use.
            optimizer: Optimizer to use, eg SGD/Adam/etc.
            train_data_loader: Training dataloader.
            val_data_loader: Validation dataloader.
            device: Device to do training/validation on.
            log_every_n_batches: Controls frequency of logging training metrics.
            skip_val: If True, this skips validation.
        """
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer
        self.train_data_loader = train_data_loader
        self.val_data_loader = val_data_loader
        self.device = device
        self.log_every_n_batches = log_every_n_batches
        self.skip_val = skip_val

    def perform_validation(self) -> EvalMetrics:
        if self.skip_val:
            print(f"Skipping validation (self.skip_val={self.skip_val})")
            return EvalMetrics(
                torch.tensor([0.0]), torch.tensor([0.0]), torch.tensor([0.0]),
                0.0, OperatingPointMetrics(0.0, 0.0, 0.0, 1.0)
            )
        return eval_model(self.model, self.val_data_loader, device=self.device)

    def train(self, total_num_epochs: int) -> TrainMetadata:
        """Trains self.model using given self.criterion and self.optimizer.
        Args:
            total_num_epochs: Number of training epochs to do.
        Returns:
            train_metadata: Struct that contains training/val metadata. See: `TrainMetadata`
        """
        self.model = self.model.to(device=self.device)
        self.model.train()
        # Tip: populate `losses, train_accs, train_accs_pos_class` after every `self.log_every_n_batches` batches.
        # `train_accs` is the classification accuracy. To compute this, take the model
        #   predicted probabilities, and use the binary classification rule with threshold=0.5:
        #     positive_class if predicted_prob >= 0.5 else negative_class
        # `train_accs_pos_class` is like `train_accs`, but computed only over the positive class. This is useful because
        #   in our dataset, there is significant class imbalance: the positive class ("is_faulty") is a very rare.
        # After each training epoch, populate `all_val_metrics` by appending the output of `self.perform_validation()`.
        losses = []
        train_accs = []
        train_accs_pos_class = []
        all_val_metrics = []
        # BEGIN YOUR CODE
        # END YOUR CODE
        return TrainMetadata(
            losses=losses,
            train_accs=train_accs,
            train_accs_pos_class=train_accs_pos_class,
            all_val_eval_metrics=all_val_metrics,
            num_model_parameters=count_model_parameters(self.model),
        )
