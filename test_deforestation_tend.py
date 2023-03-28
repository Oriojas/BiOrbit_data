import deforestation_tend as deforest

FILE_META = '/home/oscar/GitHub/BiOrbit_data/img_data/data.json'
FILE_NDVI = "/home/oscar/GitHub/BiOrbit_data/img_input/2023-03-14-LC09_B2_B3_B4_B5_multiband_NDVI_masked_added.TIF"

data_process_obj = deforest.DataProcess(file_meta=FILE_META,
                                        ndvi_tif=FILE_NDVI)

data_process_obj.process_meta(reg_date="2023-05-30",
                              view_plot=True,
                              log=True,
                              plot_name="plot_tend")

data_process_obj.process_ndvi_tif(view_plot=True)
