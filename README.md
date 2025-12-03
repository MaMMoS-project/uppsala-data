# DFT and spindynamics data

This repository contains DFT and spindynamics data computed at Uppsala university as part of [MaMMoS](https://https://mammos-project.github.io/).

## Folder structure

All simulation data is stored in the `data/` directory. The content of each
dataset is structured as follows:

```yaml
chemical-formula_optional-description:
  RSPt:
    README.md  # optional
    common_input:
      - atomdens
      - kmap
      - spts
      - symcof
      - symt.inp
    gs_x:
      - data
      - hist OR out_MF
      - out_last
    gs_y:  # optional
      - data
      - hist OR out_MF
      - out_last
    gs_z:
      - data
      - hist OR out_MF
      - out_last
    Jij:
      - data
      - green.inp-*
      - out-*
      - out_last
  UppASD:
    README.md  # optional
    MC_1:
      - jfile
      - momfile
      - posfile
      - inpsd.dat
      - M(T)
      - output.csv
    MC_2:  # optional
      - jfile
      - momfile
      - posfile
      - inpsd.dat
      - M(T)
      - output.csv
  DOSCAR  # optional
  README.md  # optional
  intrinsic_properties.yaml
  structure.cif
```

Comments:
- The directory name should be a reduced chemical formula and can optionally
  contain a description. Examples:
  - `Nd2Fe14B`
  - `Nd2Fe14B_comment`
  - `Nd2Fe14B_method1`
  - `Nd2Fe14B_method2`
  - $`(Nd_{1-x} Ce_x)_2 Fe_{14}B`$ with x=0.25 -> `Nd1.5Ce0.5Fe14B`
- `RSPt/common_input` contains input files required for all RSPt runs.
  Together with data and optionally one
  green.inp-* it is sufficient to rerun the DFT calculations.
- Only `gs_x` and `gs_z` are required. The directories contain
  either `hist` OR `out_MF` depending on how `MAE` is calculated.
- Optional README.md files should be human readable and will not be parsed
  when validating a dataset.
- `intrinsic_properties.yaml` is created with
  `mammos_entity.io.entities_to_file` and contains entities
  SpontaneousMagneticPolarisation `Js`, SpontaneousMagnetization `Ms`, MagnetocrystallineAnisotropyEnergy `MAE` and
  CurieTemperature `Tc`.
- `MC_*/output.csv` is created with `mammos_entity.io.entities_to_file` and contains
  entities ThermodynamicTemperature `T`, SpontaneousMagnetization `Ms`, and
  IsochoricHeatCapacity `Cv`.
- If Tc is derived from Binder cumulants, two directories `MC_1` and `MC_2` need to be
  present, otherwise a single `MC_1` is sufficient. If multiple directories are present,
  `MC_1` should contain the largest system size, so that the most accurate simulation
  can always be found in `MC_1`.
- `green.inp-*` and `out-*` are present in pairs; no further constraints are applied to the suffixes.

## Contributing data

Data contribution is not yet possible. This section will be updated once data
can be accepted.

## Acknowledgements

This software has been supported by the European Union’s Horizon Europe research and innovation programme under grant agreement No 101135546 [MaMMoS](https://mammos-project.github.io/).
