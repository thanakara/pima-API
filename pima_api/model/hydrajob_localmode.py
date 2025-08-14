import logging
import time

import hydra
from omegaconf import DictConfig, OmegaConf

from pima_api.constant import Filepath
from pima_api.model.trainjob_localmode import fit_report_and_serialize

log = logging.getLogger(__name__)


@hydra.main(
    config_path=Filepath.CONFIGPATH.value.as_posix(),
    config_name="config",
    version_base=None,
)
def experiment_run(config: DictConfig) -> None:
    OmegaConf.resolve(config)
    logging.info("Starting the job")
    time.sleep(1.5)
    model = fit_report_and_serialize(config)
    logging.info(model.__class__.__name__)
    time.sleep(1.5)
    logging.info("Job ended")
    time.sleep(0.5)


if __name__ == "__main__":
    experiment_run()
