# DFT and spindynamics data

This repository contains DFT and spindynamics data computed at Uppsala university as part of [MaMMoS](https://https://mammos-project.github.io/).

## Folder structure

All simulation data is stored in the `data/` directory. The content of each
dataset must follow the schema defined in [dataset-schema.yaml](dataset-schema.yaml).

Schema compliance is ensured via CI and [mammos-parser](https://github.com/MaMMoS-project/mammos-parser).

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
- `intrinsic_properties.yaml` and `MC_*/thermal.csv` have a defined structure and are best creating with with `mammos-parser`.
- If Tc is derived from Binder cumulants, two directories `MC_1` and `MC_2` need to be
  present (optionally a third `MC_3` may also be present), otherwise a single `MC_1` is sufficient. If multiple directories are present,
  `MC_1` should contain the largest system size, so that the most accurate simulation
  can always be found in `MC_1` (this rule is not enforced by the parser).
- `green.inp-*` and `out-*` are present in pairs; no further constraints are applied to the suffixes.

## Contributing data

To add a new dataset (or update an existing one) please follow the following steps:

1. [First time only] Clone repository (most convenient with an SSH key as explain in the [GitHub
   documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)).

   ```
   git clone git@github.com:MaMMoS-project/uppsala-data.git
   ```

   Alternatively, use `git clone https://github.com/MaMMoS-project/uppsala-data.git` Note: you cannot push over
   https using your username+password. Instead, you have to create a
   [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

   Install [pixi](https://pixi.prefix.dev/latest/installation/), which is used to managed dependencies.

   Then go into the new directory: `cd uppsala-data`

2. Switch to the correct branch:

   If you are adding a new dataset create a new branch with `git checkout -b
   BRANCH_NAME`. Pick a suitable BRANCH_NAME, e.g.
   `new-dataset-<chemical-composition>`.

   If you want to contribute to an open PR switch to that branch: `git checkout
   BRANCH_NAME`. The BRANCH_NAME is displayed in the PR page on GitHub. Example:
   to contribute to https://github.com/MaMMoS-project/uppsala-data/pull/3 run
   `git checkout new-dataset`.

3. Add new/updated files: copy files/directories into the `data/<chemical_composition>`
   subdirectory, rename files/directories, delete files/directories as needed.

   For a new dataset you need to create that directory first. You
   can also add additional information to the subdirectory name, e.g.
   `<chemical_composition>_<other_information>`, which can e.g. be useful if the
   multiple datasets exist for the same chemical composition.

   Once you have all raw data, use `mammos-parser` to check for consistency:

   ```
   pixi run mammos-parser uppsala-data validate-dataset data/<chemical_composition>
   ```

   This will inform you about wrong/missing data. Fix all issues until you are left with just complaints
   about the files `intrinsic_properties.yaml`, `thermal.csv` and `metadata.yaml`. These three files can
   (and should) be auto-generated with the following command:

   ```
   pixi run mammos-parser uppsala-data generate-derived-files data/<chemical_composition>
   ```

   Once that has finished, re-run the validation, which should now pass:

   ```
   pixi run mammos-parser uppsala-data validate-dataset data/<chemical_composition>
   ```

   Once you have all data add and commit it:

   ```
   git add data/<chemical_composition>
   git commit -m "<put your commit message here>"
   # example: git commit -m "New dataset <chemical composition>"
   ```

4. Push the changes: `git push`; for a new branch the push will fail, copy the
   right push command displayed in the error message.

5. Create a new pull request (PR) on GitHub if it does not exist yet.

   If you have pushed recently, GitHub will show a message to create a new PR,
   just click on that button and follow the instructions. Otherwise, go to the
   repository -> Pull requests -> New pull requests -> choose your branch for
   `compare` and create the PR.

6. A few CI jobs will automatically run after each push and check that the
   dataset follows the required format. Check the pipeline summary displayed in
   the PR overview page. If any job is failing look at the job log to see where
   the problem is coming from.

   *Note for new PRs*: Each PR should have a file describing the changes introduced
   in tha PR in the `changes/` subdirectory, the
   [changes/README.md](changes/README.md) explains more  details. One CI job
   checks for the presence of that file and will fail if it is missing or does
   not have the correct name. So for new PRs that typically don't have the file
   yet this job will fail.

7. Repeat steps 3 – 6 until all tests pass, then select a reviewer on the PR
   overview page.



## Acknowledgements

This software has been supported by the European Union’s Horizon Europe research and innovation programme under grant agreement No 101135546 [MaMMoS](https://mammos-project.github.io/).
