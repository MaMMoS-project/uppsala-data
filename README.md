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
    gs_y:
      - ...
    gs_z:
      - ...
    Jij:
      - data
      - green.inp-*
      - out-*
      - out_last
  UppASD:
    README.md  # optional
    MC:
      - jfile
      - momfile
      - posfile
      - inpsd.dat
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
- `common_rspt_input` contains input files required for rspt, shared across all
  DFT calculations for the material. Together with data and optionally one
  green.inp-* it is sufficient to rerun the DFT calculations.
- Only two of `gs_x`, `gs_y` and `gs_z` are required. The directories contain
  either `hist` OR `out_MF` depending on how `MAE` is calculated.
- Each directory can optionally contain a README.md file, which should be human
  readable but not machine readable.
- `intrinsic_properties.yaml` is created with
  `mammos_entity.io.entities_to_file` and contains entities
  SpontaneousPolarization `Js`, MagnetocrystallineAnisotropyEnergy `MAE` and
  CurieTemperature `Tc`.
- `MC/output.csv` is created with `mammos_entity.io.entities_to_file` and contains
  entities ThermodynamicTemperature `T`, SpontaneousMagnetization `Ms`, and
  IsochoricHeatCapacity `Cv`.
- `green.inp-*` and `out-*` are present in pairs; `*` denotes consecutive numbers.

## Contributing data

Data contribution is not yet possible. This section will be updated once data
can be accepted.

## Acknowledgements

This software has been supported by the European Union’s Horizon Europe research and innovation programme under grant agreement No 101135546 [MaMMoS](https://mammos-project.github.io/).
