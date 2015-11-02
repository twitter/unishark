import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(cur_dir, os.pardir))
import unittest
import logging
import unishark
from time import sleep
import threading

log = logging.getLogger(__name__)


class MyTestClass5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\t%s.%s.setUpClass' % (__name__, cls.__name__))
        sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        print('\t%s.%s.tearDownClass' % (__name__, cls.__name__))
        sleep(0.1)

    def test_11(self):
        """Here is test_11's doc str"""
        log.info('Here is logging of test_11')
        sleep(2)
        self.assertEqual(1, 1)

    def test_12(self):
        """Here is test_12's doc str"""
        log.info('Here is logging of test_12')
        sleep(2)
        self.assertEqual(1, 1)


class MyTestClass6(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\t%s.%s.setUpClass' % (__name__, cls.__name__))
        sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        print('\t%s.%s.tearDownClass' % (__name__, cls.__name__))
        sleep(0.1)

    def test_13(self):
        """Here is test_13's doc str"""
        log.info('Here is logging of test_13')
        sleep(2)
        self.assertEqual(1, 1)

    def test_14(self):
        """Here is test_14's doc str"""
        log.info('Here is logging of test_14')
        sleep(2)
        self.assertEqual(1, 1)


class MyTestClass7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\t%s.%s.setUpClass' % (__name__, cls.__name__))
        sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        print('\t%s.%s.tearDownClass' % (__name__, cls.__name__))
        sleep(0.1)

    def test_15(self):
        """Here is test_15's doc str"""
        log.info('Here is logging of test_15')
        sleep(2)
        self.assertEqual(1, 1)

    def test_16(self):
        """Here is test_16's doc str"""
        log.info('Here is logging of test_16')
        sleep(1)
        self.assertEqual(1, 1)


class MyTestClass8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\t%s.%s.setUpClass' % (__name__, cls.__name__))
        sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        print('\t%s.%s.tearDownClass' % (__name__, cls.__name__))
        sleep(0.1)

    @unishark.data_driven(left=list(range(9)))
    @unishark.data_driven(right=list(range(9)))
    def test_17(self, **param):
        """Test cross-multiply data-driven"""
        l = param['left']
        r = param['right']
        log.info('%d x %d = %d' % (l, r, l * r))

    @unishark.multi_threading_data_driven(10, time=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    def test_18(self, **param):
        log.info('Thread %d sleeps %.1f sec.' % (threading.current_thread().ident, param['time']))
        sleep(param['time'])

    @unishark.multi_threading_data_driven(3, time=[1, 2, 1, 1, 1, 2])
    def _sleep_with_errors(self, **param):
        if param['time'] == 1:
            log.info('Thread %d sleeps %.1f sec.' % (threading.current_thread().ident, param['time']))
            sleep(param['time'])
        else:
            raise AssertionError('Error thrown in thread %d.' % threading.current_thread().ident)

    def test_19(self):
        self._sleep_with_errors()

    @unishark.multi_threading_data_driven(2, time1=[1, 1])
    @unishark.multi_threading_data_driven(3, time2=[1, 2, 1])
    def test_20(self, **param):
        time = param['time1'] * param['time2']
        if time == 1:
            log.info('Thread %d sleeps %.1f sec.' % (threading.current_thread().ident, time))
            sleep(time)
        else:
            raise AssertionError('Error thrown in thread %d.' % threading.current_thread().ident)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    result = unishark.BufferedTestRunner().run(suite, name='mytest3', max_workers=3)
    reporter = unishark.HtmlReporter(dest='log')
    reporter.report(result)