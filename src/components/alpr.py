from openalpr import Alpr
from argparse import ArgumentParser
from loguru import logger
from src.components.models import ResponseAlpr
from src.components.error import Error


def get_plates(imagen):
 
    alpr = None
    country = 'us'
    config = '/etc/openalpr/openalpr.conf'
    runtime_data = '/usr/share/openalpr/runtime_data'
    try:
        logger.info('starting ALPR')
        alpr = Alpr(country, config, runtime_data)

        if not alpr.is_loaded():
            logger.warning('"Error loading OpenALPR')
            return ResponseAlpr(message='Error loading OpenALPR', code=Error.ERROR_FALTAL.value)

        else:
            logger.info("Using OpenALPR " + alpr.get_version())
            alpr.set_top_n(7)
            alpr.set_default_region("wa")
            alpr.set_detect_region(False)
            logger.info("Let's open the file")
            results = alpr.recognize_array(imagen)

            logger.info("Image size: %dx%d" %
                        (results['img_width'], results['img_height']))
            logger.info("Processing Time: %f" % results['processing_time_ms'])
            logger.info(results['results'])

            if(len(results['results']) > 0):
                return ResponseAlpr(code=Error.OK.value, message='Everything ok', result=results['results'])
            else:
                return ResponseAlpr(code=Error.NO_PLATE_FOUND.value, message='Any plates were found')

    except BaseException as excep:
        logger.warning('Exception loading OpenALPR')
        return ResponseAlpr(message='Error loading OpenALPR'+str(excep), code=Error.ERROR_FALTAL.value)

    finally:
        if alpr:
            logger.debug('Turning off ALPR')
            alpr.unload()
