import os # Should be already imported

STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_SECRET_KEY", "pk_test_hWSfnxMESAc3HFaBA9N1xMEx")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_dSyoBcoboNJouZ6tVC5Jqqk7")