import logging
import time

import hydra
from omegaconf import DictConfig, OmegaConf

from pima_api.constant import Filepath
from pima_api.model.job import randf_fit_report_and_serialize

log = logging.getLogger(__name__)


@hydra.main(
    config_path=Filepath.CONFIGPATH.value.as_posix(),
    config_name="config",
    version_base=None,
)
def run(config: DictConfig) -> None:
    OmegaConf.resolve(config)
    rand_f = randf_fit_report_and_serialize(config=config)
    log.info("Serialize and Report")

    return rand_f


if __name__ == "__main__":
    run()
