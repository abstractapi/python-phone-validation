# AbstractAPI python-phone-validation library

Integrate the powerful [Phone Validation API from Abstract](https://www.abstractapi.com/phone-validation-api) in your Python project in a few lines of code.

Abstract's Phone Number Validation and Verification API is a fast, lightweight, modern, and RESTful JSON API for determining the validity and other details of phone numbers from over 190 countries.

It's very simple to use: you only need to submit your API key and a phone number, and the API will respond as assessment of its validity, as well as additional details like the carrier details, line type, region and city details, and more.

Validating and verifying phone numbers is a critical step to reducing the chances of low quality data and fraudulent or risky users in your website or application.

# Documentation

## Supported Python Versions

This library supports the **Python version 3.6** and higher.

## Installation

You can install **python-phone-validation** via PyPi or by downloading the source.

### Via Composer:

**python-phone-validation** is available on Packagist as the
[`abstract-python-phone-validation`](https://pypi.org/project/abstract-python-phone-validation/)  package:

```bash
pip install abstract-python-phone-validation
```

## API key

Get your API key for free and without hassle from the [Abstact website](https://app.abstractapi.com/users/signup?target=/api/phone-validation/pricing/select).

## Quickstart

### Verify phone

```python
# Verify phone using Abstract's Phone  Validation and Verification API and Python
from python_phone_validation import AbstractPhoneValidation

PHONE_VAL_API_KEY =  "YYYYYY"; # Get your API Key from https://app.abstractapi.com/api/phone-validation/documentation

AbstractPhoneValidation.configure(PHONE_VAL_API_KEY)
AbstractPhoneValidation.verify("14154582468")
```

## API response

The API response is returned in a `IpGeolocationData` object.

| PARAMETER | TYPE | DETAILS |
| - | - | - |
| number | String | The phone number submitted for validation and verification. |
| valid | Boolean | Is true if the phone number submitted is valid. |
| local_format | String | The local or national format of the submitted phone number. For example, it removes any international formatting, such as "+1" in the case of the US. |
| international_format | String | The international format of the submitted phone number. This means appending the phone number's country code and a "+" at the beginning. |
| country_name | String | The name of the country in which the phone number is registered. |
| country_code | String | The country's two letter ISO 3166-1 alpha-2 code. |
| country_prefix | The country's calling code prefix. |
| registered_location | String | As much location details as are available from our data. This can include the region, state / province, and in some cases down to the city. |
| carrier | String | The carrier that the number is registered with. |
| line_type | String | The type of phone number. The possible values are: Landline, Mobile, Satellite, Premium, Paging, Special, Toll_Free, and Unknown. |

## Detailed documentation

You will find additional information and request examples in the [Abstract help page](https://app.abstractapi.com/api/phone-validation/documentation).

## Getting help

If you need help installing or using the library, please contact [Abstract's Support](https://app.abstractapi.com/api/phone-validation/support).

For bug report and feature suggestion, please use [this repository issues page](https://github.com/abstractapi/python-phone-validation/issues).

# Contribution

Contributions are always welcome, as they improve the quality of the libraries we provide to the community.

Please provide your changes covered by the appropriate unit tests, and post them in the [pull requests page](https://github.com/abstractapi/python-phone-validation/pulls).

## Setup

To install the requirements, run:

```bash
python3 setup.py install --user
```

Once you implementer all your changes and the unit tests, run the following command to run the tests:

```bash
PHONE_VAL_API_KEY=YYYYYY python3 tests/test_python_phone_validation.py
```
