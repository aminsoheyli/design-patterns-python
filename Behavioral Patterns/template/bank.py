from abc import ABC, abstractmethod


class AuditTrail:
    def record(self):
        print("Audit")


class Task(ABC):
    def __init__(self, audit_trail=AuditTrail()):
        self.__audit_trail: AuditTrail = audit_trail

    def execute(self):
        self.__audit_trail.record()
        self._do_execute()

    @abstractmethod
    def _do_execute(self):
        pass


class TransferMoneyTask(Task):
    def _do_execute(self):
        print('Transfer Money')


class GenerateReportTask(Task):
    def _do_execute(self):
        print('Generate Report')


if __name__ == '__main__':
    task = TransferMoneyTask()
    task.execute()
