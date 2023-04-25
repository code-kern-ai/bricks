---
name: Bug Report
about: Describe a bug or misunderstanding in an existing bricks module
title: "[BUG] - Short description and module name"
labels: bug
assignees: ''

---

## What module did you encounter a bug with?
Please specify the name of the brick module that you are encounting errors with. If you have, you can also specify the link to the issue page of the brick, which you can access by simply clicking the `GitHub` button on each brick page.

## Please describe the bug you observed with this module.
Besides a description, it would be really helpful to also include an example input and both the actual and the expected output. Also include the necessary information for reproducibility, e.g. the tokenizer you used.

For example: 

### Description
The rgb regex in the color code extraction currently does not match with the rgb + alpha format, which is "rgba".

### Input:
I used the default ```en_core_web_sm``` tokenizer and the following input string:
```css
element.style {
    line-height: 80px;
    background-color: rgba(255, 99, 71, 0.5);
}
```
### Expected output:
```python
{"extractedColorCodes": [["color", 14, 22]]}
```

### Actual output:
```python
{"extractedColorCodes": []}
```


## Do you already have a fix for that?
If so, please share it here. 

For example:

Extend the rgb regex to also include rgba. So I would change
  ```python
  rgb_regex = re.compile(r"(rgb)\([^\)]*\)")
  ```
to this
  ```python
  rgb_regex = re.compile(r"(rgba|rgb)\([^\)]*\)")
  ```

## Additional context

Add any other context or screenshots about the bug here. You can also start a few discussion points here that you feel need clarification.
