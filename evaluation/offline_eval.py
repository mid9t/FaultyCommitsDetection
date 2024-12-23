import sklearn.metrics
import torch
from sklearn.metrics import precision_recall_curve
from tqdm import tqdm
import numpy as np

from evaluation.eval_structs import PredictionMetadata, OperatingPointMetrics, EvalMetrics


def predict_samples(model: torch.nn.Module, dataloader: torch.utils.data.DataLoader, device: torch.device) -> PredictionMetadata:
    """Given a model and a dataloader, generates model predictions on each sample in dataloader.

    Tip: as the model.forward() returns logits, you will want to call `torch.nn.functional.sigmoid(logits)` to transform
        the logits to probability scores.

    Args:
        model:
        dataloader: Dataloader to run inference on.
            Take care that this produces batched inputs.
        device: Device to run inference on. Ex: CPU or cuda:0

    Returns:
        prediction_meta: Struct containing all inference results, along with ground truth labels.
            See `PredictionMetadata` for more details.

    """
    # Tip: remember to call `model.eval()`!
    model = model.eval()
    # BEGIN YOUR CODE
    # END YOUR CODE
    return PredictionMetadata(
        pred_probs=None,
        labels_gt=None,
    )


def compute_eval_metrics(prediction_meta: PredictionMetadata) -> EvalMetrics:
    """Computes evaluation metrics.

    Args:
        prediction_meta: Contains model predictions and ground-truth labels.

    Returns:
        eval_metrics: evaluation metrics that we care about:
            precision-recall curve
            average precision
            operating-point metrics

    """
    # BEGIN YOUR CODE
    # END YOUR CODE
    return EvalMetrics(
        precisions=None,
        recalls=None,
        thresholds=None,
        average_precision=0.0,
        metrics_op=None,
    )


def eval_model(
        model: torch.nn.Module,
        dataloader_test: torch.utils.data.DataLoader,
        device: torch.device
) -> EvalMetrics:
    """Given a model and test dataset, evaluates the model on the test dataset.

    Args:
        model:
        dataloader_test:
        device:

    Returns:
        eval_metrics:
    """
    prediction_meta = predict_samples(model, dataloader_test, device)
    return compute_eval_metrics(prediction_meta)


def compute_operating_point_metrics_max_f1(
        precisions: torch.Tensor,
        recalls: torch.Tensor,
        thresholds: torch.Tensor
) -> OperatingPointMetrics:
    """Calculate eval metrics at the operating point (aka threshold) that maximizes F1 score.
    Precisions/recalls/thresholds are computed from: sklearn.metrics.precision_recall_curve()

    Args:
        precisions:
        recalls:
        thresholds:

    Returns:
        operating_point_metrics: eval metrics at the threshold that maximizes the F1 score.

    """
    # BEGIN YOUR CODE
    # END YOUR CODE
    return OperatingPointMetrics(
        precision_op=0.0,
        recall_op=0.0,
        f1_score_op=0.0,
        threshold_op=1.0,
    )


def compute_operating_point_metrics_at_threshold(
        precisions: torch.Tensor,
        recalls: torch.Tensor,
        thresholds: torch.Tensor,
        threshold_op: float,
) -> OperatingPointMetrics:
    """Compute eval metrics at a specific input threshold.
    Precisions/recalls/thresholds are computed from: sklearn.metrics.precision_recall_curve()

    Args:
        precisions:
        recalls:
        thresholds:
        threshold_op: Threshold to calculate precision/recall/f1 for.
            Note that `threshold_op` will in general not be exactly in `thresholds`.
            In this case, use the precision/recall values corresponding to the first threshold
            in `thresholds` where `threshold >= threshold_op`.

    Returns:
        operating_point_metrics: Eval metrics at the given threshold (`threshold_op`).
    """
    # BEGIN YOUR CODE
    # END YOUR CODE
    return None
