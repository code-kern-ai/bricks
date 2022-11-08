![](identifier.svg)

<p align="center">
    <b>Open-source natural language enrichments at your fingertips.</b>
</p>

Browse [bricks](https://bricks.kern.ai) to find gold nuggets for your projects; enrich your texts e.g. with sentence complexity estimations, sentiment analysis, and more.

![](hero.svg)

Modules that are added in this repository aren't automatically available online; they must be added in our content management system by hand.

## Table of contents
- [What are classifiers and extractors?](#what-are-classifiers-and-extractors)
- [Getting started](#getting-started)
- [Contributing](#contributing)
- [refinery](#refinery)
- [Regular updates and newsletter](#regular-updates-and-newsletter)
- [License](#license)

## What are classifiers and extractors?
We generally summarize them as modules in this repository.

### Classifiers
Classifiers are modules that summarizes a given text into a specific category. For example, a module that classifies a text into the category `news` or `blog` would go into this folder. It can also be about enrichments, e.g. to detect languages and such.

### Extractors
Extractors are modules that retrieve specific information from a given text. For example, a module that extracts the author of a text would go into this folder.

### Other modules
In the future, we'll also add modules such as generators, which create new content based on a given text, or filtersets for refinery with pre-defined content.

## Getting started
You can access the modules of this repository in [bricks](https://bricks.kern.ai). If you want to host the modules yourself, you can do so by following the steps below.

1. Clone this repository
2. (optional) Create a virtual environment
3. Install the dependencies (`pip install -r requirements.txt`)
4. Run the FastAPI server (`uvicorn api:api`)

## Contributing
Please look into our [contribution guidelines](CONTRIBUTING.md) to get started. If you have any questions, please reach out to us anytime on [Discord](https://discord.gg/qf4rGCEphW).

If the content of this repository is helpful, please leave a star ⭐️. Also, make sure to check out [refinery](#refinery).

## refinery
Check out our main product [refinery](https://github.com/code-kern-ai/refinery), which is another open-source project helping you to scale, assess and maintain your training data. You can use the modules from bricks right away in refinery.

## Regular updates and newsletter
We regularly update bricks with new modules (we aim to add two modules per week, if not more). If you want to stay up to date, you can subscribe to our [newsletter](https://www.kern.ai/#email-address).

## License
This repository is licensed under the Apache License, Version 2.0. View a copy of the [License file](LICENSE).
