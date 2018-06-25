#!/usr/bin/env python

import datetime
from .print_helper import Print
import time
import getpass


def main():
    demo()


def demo():
    today = datetime.date.today()
    ninety_days = today + datetime.timedelta(days=90)

    print('Fluidkeys v0.9.1')

    print()
    print("Testing software configuration")
    print()
    Print.tick('Team best practice policy is up to date')
    Print.tick('11 team member keys are up to date')
    Print.tick('Team aliases are up to date (everyone@, admin@)')
    Print.tick('Git is configured to sign commits automatically')
    time.sleep(0.2)

    print()
    print("Testing PGP key for paul@fluidkeys.com")
    print()

    time.sleep(1)
    Print.tick('Has a separate signing subkey')
    time.sleep(0.3)
    Print.tick('Has a separate encryption subkey')
    time.sleep(0.3)
    Print.tick('All keys use strong encryption algorithms')
    time.sleep(0.3)
    Print.tick('Encrypted backups are up to date')
    time.sleep(0.3)
    Print.cross('Primary key expires between 30 days and 1 year')
    time.sleep(0.3)
    Print.cross('Signing subkey expires between 30 days and 1 year')
    time.sleep(0.3)

    print()
    print("Fluidkeys is about to perform these tasks:")
    print()
    time.sleep(1)

    Print.bullet('Extend primary key expiry for 90 days ({})'.format(
        ninety_days.isoformat()
    ))
    Print.bullet('Extend signing key expiry for 90 days ({})'.format(
        ninety_days.isoformat()
    ))
    Print.bullet('Push updated key to 11 team members'.format(
        ninety_days.isoformat()
    ))
    print()
    getpass.getpass('Enter PGP key password to continue: ')

