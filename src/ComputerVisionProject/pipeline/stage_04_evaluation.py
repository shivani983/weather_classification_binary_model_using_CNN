from ComputerVisionProject.config.configuration import ConfigurationManager
from ComputerVisionProject.components.evaluation import Evaluation
from ComputerVisionProject import logger




STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()