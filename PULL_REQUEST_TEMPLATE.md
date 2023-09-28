refinery
- [ ] Tested by creator on refinery
- [ ] Tested by reviewer on refinery
- [ ] Ensured that output of brick conforms with refinery structure (to be checked by reviewer)

API
- [ ] Tested by creator on localhost:8000/docs
- [ ] Tested by reviewer on localhost:8000/docs

common code
- [ ] Common code tested in notebook/ script by creator
- [ ] Common code tested in notebook/ script by reviewer
- [ ] Common code contains docstrings and type hints

additional points:
- [ ] Docstring and README is existing
- [ ] Import statements (in `__init__.py`)
- [ ] Added dependency to requirements.txt
- [ ] Added dependency to Issue for refinery env [here](https://github.com/code-kern-ai/refinery/issues/166)
- [ ] Published brick to Strapi CMS (locally)


Testing procedure: 
When testing in refinery, please ensure that the output of the brick conforms with the structure of refinery. 
For `extraction` bricks, this would be a tuple like `("label", span_start, span_end)`.
For `classification` bricks, this would be a string representing a label.
For `generator` bricks, this would either be a float, interger or string.

When testing the bricks, try to avoid using only one source of data. Meaning that you should not only use the `clickbait` sample
project, but also different texts with longer or more complex strings. 
A small refinery example project with a variation of texts can be downloaded [here](https://drive.google.com/file/d/1fP-Ev3rkJ8yQV7Km_9px3AfUyZzBAXpv/view?usp=sharing).


