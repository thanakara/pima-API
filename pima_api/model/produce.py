import logging

import hydra
import pandas as pd
from omegaconf import DictConfig, OmegaConf

from pima_api.constant import Filepath
from pima_api.model.job import fit_report_and_serialize

log = logging.getLogger(__name__)


@hydra.main(
    config_path=Filepath.CONFIGPATH.value.as_posix(),
    config_name="config",
    version_base=None,
)
def run(config: DictConfig) -> None:
    OmegaConf.resolve(config)
    rand_f = fit_report_and_serialize(config=config)
    params = rand_f.get_params()
    log.info("@_Serialize job")
    log.info(pd.DataFrame(params.values(), index=params.keys(), columns=["params_"]))
    return rand_f


if __name__ == "__main__":
    run()
