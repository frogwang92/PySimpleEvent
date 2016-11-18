import subject


class Observer(object):
    def __init__(self):
        pass

    def notify(self, args):
        print "notified"


class Observer2(object):
    def __init__(self):
        pass

    def notify(self, args):
        print "obs2 notified"


class Engine(subject.Subject):

    def __init__(self):
        super(Engine, self).__init__()
        self.test_event = subject.Event()

    def update_event1(self):
        self.update(self.test_event, [])


engine = Engine()
ob1 = Observer()
ob2 = Observer2()

engine.subscribe(engine.test_event, ob1.notify)
engine.subscribe(engine.test_event, ob2.notify)
engine.update_event1()

engine.unsubscribe(engine.test_event, ob1.notify)
engine.update_event1()