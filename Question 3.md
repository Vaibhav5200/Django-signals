Yes, by default, Django signals (like post_save or pre_save) run in the same database transaction as the caller. If an exception occurs after a signal is fired, the entire transaction, including the signal handler, is rolled back.

To prove this, we can use Django’s transaction module to simulate a database transaction, trigger a signal, and see how both the signal handler and the main code are affected when the transaction is rolled back.
