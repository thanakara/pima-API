import hydra
from constant import Filepath
from data.preprocess import stratify_split_dataset
from omegaconf import DictConfig, OmegaConf


@hydra.main(
    config_path=Filepath.CONFIGPATH.value.as_posix(),
    config_name="config",
    version_base=None,
)
def main(config: DictConfig) -> None:
    OmegaConf.resolve(config)
    X_train, *_ = stratify_split_dataset(
        datapath=Filepath.DATAPATH.value, train_size=config.train_size, seed=config.seed
    )
    print(X_train.shape)


if __name__ == "__main__":
    main()
