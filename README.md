# final_proj_faulty_commit

The final project for Data C182 Fall 2024.

**For students**: start off by cloning/downloading this repo, uploading to your Google drive, and running the `final_project.ipynb` notebook in Colab.

**Project spec**: https://docs.google.com/document/d/1erKfrMXIY_JkPB_648wyaTXP89Llo4MyD68l_pZRwZo/edit?tab=t.0#heading=h.i522cvq4jmw

Maintainers:
- Eric Kim (ekim555@berkeley.edu)
- Naveen Ashish (nashish@berkeley.edu)

# (Internal notes)
The following is for course staff only.

## Gradescope Autograder

To create the Gradescope autograder, run the following:

```
cd final_proj_faulty_commit_sol/
./scripts/create_autograder.sh
```
This will create a new file `final_proj_faulty_commit_sol/autograder.zip`, which you will then upload to Gradescope in the "Configure Autograder" section.

## Generate student-facing version

The student-facing github repo (`final_proj_faulty_commit_student`) is generated from the "solution" repo via automated scripts.

To generate the student-facing repo (eg with solutions removed), run the following:

```
# First, make sure that the `final_proj_faulty_commit_student` repo exists in the following directory structure:
#   some_parent_dir/final_proj_faulty_commit_student
#   some_parent_dir/final_proj_faulty_commit_sol
# Then, run the following:
cd some_parent_dir/final_proj_faulty_commit_sol
./scripts/generate_student_version_runner.sh

# This will update `some_parent_dir/final_proj_faulty_commit_student`, so then you will want to commit+push those changes:
cd ../final_proj_faulty_commit_student
git checkout -b fa24-yourname-some-name
git add -A
git commit -m "Update student-facing code"
git push origin fa24-yourname-some-name

# Then, click the resulting github link, and merge it into the main branch.
```

Tip: If you make any changes to the student-facing code (that breaks backwards compatibility) after the project has been released, you should probably make an Ed announcement to tell students to re-download the code/notebook.

Important: anything you push to `final_proj_faulty_commit_student` will be visible to students! So, take extra care when updating this repo. On the other hand, `final_proj_faulty_commit_sol` is a private repo, so students don't have access to this repo.
