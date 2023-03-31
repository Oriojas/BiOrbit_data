import deforestation_tend as deforest

# docker image push biorbit_data

FILE_META = "img_data/data.json"
FILE_NDVI = "img_input/2023-03-14-LC09_B2_B3_B4_B5_multiband_NDVI_masked_added.TIF"

data_process_obj = deforest.DataProcess(file_meta=FILE_META,
                                        ndvi_tif=FILE_NDVI)

data_process_obj.process_meta(reg_date="2023-05-30",
                              view_plot=False,
                              log=True,
                              plot_name="plot_tend")

data_process_obj.process_ndvi_tif(view_plot=False)
