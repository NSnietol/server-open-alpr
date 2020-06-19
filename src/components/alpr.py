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
            jpeg_bytes = open(imagen, "rb").read()
            results = alpr.recognize_array(jpeg_bytes)

            # Uncomment to see the full results structure
            # import plogger.info
            # plogger.info.plogger.info(results)

            logger.info("Image size: %dx%d" %
                  (results['img_width'], results['img_height']))
            logger.info("Processing Time: %f" % results['processing_time_ms'])

            i = 0
            for plate in results['results']:
                i += 1
                logger.info("Plate #%d" % i)
                logger.info("   %12s %12s" % ("Plate", "Confidence"))
                for candidate in plate['candidates']:
                    prefix = "-"
                    if candidate['matches_template']:
                        prefix = "*"

                    logger.info("  %s %12s%12f" %
                          (prefix, candidate['plate'], candidate['confidence']))
    except BaseException:
            logger.warning('Exception loading OpenALPR')
            return ResponseAlpr(message='Error loading OpenALPR', code=Error.ERROR_FALTAL.value)

    finally:
        if alpr:
            logger.debug('Turning off ALPR')
            alpr.unload()
