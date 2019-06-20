Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from exif import Image
>>> with open('C:\\Users\\oswal\\Pictures\\oswaldo.jpg', 'rb') as image_file:
...     my_image = Image(image_file)
...
>>> dir(my_image)
['_exif_ifd_pointer', '_gps_ifd_pointer', '_interoperability_ifd_Pointer', '_segments', 'cfa_pattern', 'color_space', 'components_configuration', 'compressed_bits_per_pixel', 'compression', 'contrast', 'custom_rendered', 'datetime', 'datetime_digitized', 'datetime_original', 'digital_zoom_ratio', 'exif_version', 'exposure_bias_value', 'exposure_mode', 'exposure_program', 'exposure_time', 'f_number', 'file_source', 'flash', 'flashpix_version', 'focal_length', 'focal_length_in_35mm_film', 'gain_control', 'get', 'get_file', 'gps_altitude', 'gps_altitude_ref', 'gps_datestamp', 'gps_latitude', 'gps_latitude_ref', 'gps_longitude', 'gps_longitude_ref', 'gps_map_datum', 'gps_satellites', 'gps_timestamp', 'gps_version_id', 'jpeg_interchange_format', 'jpeg_interchange_format_length', 'light_source', 'make', 'maker_note', 'max_aperture_value', 'metering_mode', 'model', 'orientation', 'photographic_sensitivity', 'pixel_x_dimension', 'pixel_y_dimension', 'resolution_unit', 'saturation', 'scene_capture_type', 'scene_type', 'sensing_method', 'sensitivity_type', 'sharpness', 'software', 'subject_distance_range', 'subsec_time', 'subsec_time_digitized', 'subsec_time_original', 'user_comment', 'white_balance', 'x_resolution', 'y_and_c_positioning', 'y_resolution']
>>> import pandas as pd
>>> data = pd.DataFrame(dir(my_image))
>>> datatoexcel = pd.ExcelWriter("CaracteristicasImagen.xlsx",engine='xlsxwriter')
>>> data.to_excel(datatoexcel, sheet_name='Sheet1')
>>> datatoexcel.save()
