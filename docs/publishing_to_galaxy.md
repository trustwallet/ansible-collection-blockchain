# Publishing New Versions

1. Install `antsibull-changelog` Ansible changelog tool
    ```shell
    pip install antsibull-changelog
    ```
2. Ensure all relevant PRs have provided changelog fragments, then generate a changelog entries for new version:
    ```shell
    antsibull-changelog release --version X.Y.Z --date YYYY-MM-DD
    ```
3. Update `galaxy.yml` file and `requirements.yml` example in `README.md` with the new `version` for the collection.
4. Tag the version in Git and push to GitHub:
    ```shell
    git tag -a X.Y.Z
    git push origin X.Y.Z
    ```

Additional manual steps are required when automatic publish to Ansible Galaxy
is not enabled in the repository. This requires a user who has access to the
`trustwallet.blockchain` namespace on Ansible Galaxy to publish the build artifact.

5. Run the following commands to build and release the new version on Galaxy:
     ```shell
     ansible-galaxy collection build
     ansible-galaxy collection publish ./trustwallet-blockchain-$VERSION_HERE.tar.gz
     ```

After the version is published, verify it exists on the [Trust Wallet Collection](https://galaxy.ansible.com/trustwallet/blockchain) Ansible Galaxy page.
