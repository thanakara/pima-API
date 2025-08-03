import hydra
from omegaconf import DictConfig, OmegaConf

from pima_api.constant import Filepath
from pima_api.model.job import fit_report_and_serialize


@hydra.main(
    config_path=Filepath.CONFIGPATH.value.as_posix(),
    config_name="config",
    version_base=None,
)
def main(config: DictConfig) -> None:
    OmegaConf.resolve(config)
    rand_f = fit_report_and_serialize(config=config)
    print(rand_f.__class__.__name__)


if __name__ == "__main__":
    main()
