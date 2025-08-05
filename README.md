# DFT and spindynamics data

This repository contains DFT and spindynamics data computed at Uppsala university as part of [MaMMoS](https://https://mammos-project.github.io/).

## Folder structure

## Contributing data

To add a new dataset (or update an existing one) please follow the following steps:

1. [First time only] Clone repository (most convenient with an SSH key as explain in the [GitHub
   documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)).

   ```
   git clone git@github.com:MaMMoS-project/uppsala-data.git
   ```

   Alternatively, use `git clone https://github.com/MaMMoS-project/uppsala-data.git`

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
