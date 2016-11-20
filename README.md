# PySimpleEvent

A very simple python observer pattern implementation.

Notification calls are all sync.
However, a notification queue can be implemented in class __Dispatcher__.

Samples can be found in tests.py.

To use __PySimpleEvent__:

* inherit from subject.Subject
    ```
    class Foo(subject.Subject):
* __init__ of class Subject should be called
    ```
    def __init__(self):
        super(Foo, self).__init__()
    
* define events in your class implementation
    ```
    self.test_event = subject.Event()
* subscribe event, connect the event to a slot
    ```
    subj = Foo()
    ob1 = Observer()
    subj.subscribe(subj.test_event, ob1.notify)
* fire the event
    ```
    subj.update(self.test_event, [])