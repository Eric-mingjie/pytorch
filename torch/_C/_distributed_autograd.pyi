import torch
from typing import Dict, List, Set, Any

# This module is defined in torch/csrc/distributed/autograd/init.cpp

class DistAutogradContext:
    def _context_id(self) -> int: ...
    def _recv_functions(self) -> Dict[int, Any]: ...
    def _send_functions(self) -> Dict[int, Any]: ...
    def _known_worker_ids(self) -> Set[int]: ...

def _new_context() -> DistAutogradContext: ...
def _release_context(context_id: int) -> None: ...
def _get_max_id() -> int: ...
def _is_valid_context(worker_id: int) -> bool: ...
def _retrieve_context(context_id: int) -> DistAutogradContext: ...
def _current_context() -> DistAutogradContext: ...
def _init(default_node_id: int) -> None: ...
def _get_debug_info() -> Dict[str, str]: ...
def backward(
    context_id: int,
    roots: List[torch.Tensor],
    retain_graph = False
) -> None: ...
def get_gradients(context_id: int) -> Dict[torch.Tensor, torch.Tensor]: ...
