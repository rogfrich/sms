"""
Tests for the sms package. Note that these tests will result in two messages being sent via
the configured Twilio account to the configured mobile number.
"""

import os
import sms
from pytest import raises
from twilio.base.exceptions import TwilioRestException
from sms import SMSMessage


def test_access_environment_variable_account_SID():
    # Test that we can access the settings for credentials and to / from phone numbers
    env = os.getenv("TWILIO_ACCOUNT_SID")
    assert type(env) == str and len(env) > 1


def test_access_environment_variable_auth_token():
    env = os.getenv("TWILIO_AUTH_TOKEN")
    assert type(env) == str and len(env) > 1


def test_access_environment_variable_to_number():
    env = os.getenv("TWILIO_TO_NUMBER")
    assert type(env) == str and len(env) > 1


def test_access_environment_variable_from_number():
    env = os.getenv("TWILIO_FROM_NUMBER")
    assert type(env) == str and len(env) > 1


def test_send_SMS_with_default_body():
    # Test that we can send an SMS without providing a body
    message = sms.SMSMessage()
    message.send()
    assert len(message.sid) > 0
    # if True, means that Twilio has returned a message sid, therefore the send was successful


def test_send_SMS_with_defined_body():
    # Test that we can set a particular body text for an SMS
    message = sms.SMSMessage(" THIS IS A TEST FROM THE sms TEST SUITE")
    message.send()
    assert len(message.sid) > 0
    # if True, means that Twilio has returned a message sid, therefore the send was successful
