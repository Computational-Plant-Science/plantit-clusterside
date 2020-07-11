from abc import ABC, abstractmethod

from plantit_cluster.run import Run


class Executor(ABC):
    """
    Pipeline execution engine.
    """

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def execute(self, pipeline: Run):
        pass
