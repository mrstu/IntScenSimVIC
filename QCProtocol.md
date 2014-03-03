# Quality control protocol for Integrated Scenarios data sets

UI: University of Idaho

UW: University of Washington

## Versioning, data transfer, and file conversion

* **Versioning**

    * Forcing data, parameter files and VIC model code will be versioned to keep track of changes and updates to the dataset.

    * Version numbers for datasets and model codes used to produce a data file will be included in the NetCDF `global` attributes for that data file.

        For example:

        ```
        // global attributes
            VIC_version: 4.1.2.k
            global_parameter_file:
            soil_parameter_file:
            vegetation_parameter_file:
            vegetation_library:
            forcing_dataset:
        ```

* **Data transfer**

    * **md5** checksums will be reported along with each NetCDF file to facilitate testing for data corruption during file transfers. The checksums will be reported in a simple text file in the same directory as the data files and will be posted by the party hosting the data. The text file will have the format:

        ```
        file1.nc 553bb3cfb577e8fd14bf2c8adb54c676
        file2.nc 3477c12c23724a3dd7bd2c2945550111
        .
        .
        .
        filen.nc e331b607fa61b0186e0f74149e57c80f
        ```

        The receiving party will be responsible for recalculating the checksum and ensuring that it matches that in the text file.

* **File conversion**

    The NetCDF data need to be converted to the VIC input format (ASCII in this case) and the output needs to be converted back to NetCDF. No quality control will be done on the actual values in the ASCII files. The quality control will be done before and after conversion to NetCDF. However, the following quality control procedures will be performed on the ASCII files before (input) and after (output) running VIC:

    * File count and word count to ensure that all input and output files are complete.

    * Test for 'NaN' values on all the output files.

    * Comparison of the forcings in the original NetCDF files and in the NetCDF files after conversion of the output will also serve as a quality control on the conversion, but this is discussed below.

## Sanity checks on simulations

All the following checks will be performed on the NetCDF files.

* **Consistency**

    VIC output fields contain some of the forcing variables. Ensure that these are unchanged or that the resulting values are close to the original inputs.

    * Spatial map of the differences in mean annual precipitation between the forcing and output files. These differences should be less than 1 mm/year.

* **Water balance**

    For the analysis period (duration of simulation minus the spinup period), the water balance should be checked based on the model output.

    * Spatial map of the water balance error in mm/year:

        WB_error_mean = P_mean - Runoff_mean - Baseflow_mean - Delta_storage_mean

        where Delta_storage_mean is defined as

        Delta_storage_mean = sum(soil_moisture, snow_water_equivalent)_end - sum(soil_moisture, snow_water_equivalent)_start

        where start and end are the start and end of the analysis period.

* **Range checks**

    * Spatial maps of the minimum and maximum fields for all output variables. A set of default values needs to be put together that will be used consistently.


## Reference dataset

The historic forcings and the model-generated historic simulations will serve as the reference dataset for quality control of the MACA downscaled fields. This means that the reference data itself needs to be QC'ed carefully. UI has already spent considerable effort on the forcing fields. UW will need to do the same with the derived hydrological fluxes and states (historic simulation). The historic simulation will be evaluated using the following metrics:

* **Comparison with the fields from *Livneh et al.* dataset**

    The output fields need to be compared with the model fields based on the same forcings from *Livneh et al.* (**L14** hereafter). Please make sure that the same version of the data set is used. The results will not be the same, since **L14** used a subdaily time step and different parameters. However, the results should have similar seasonal and interannual characteristics.

    * Spatial maps comparing the annual and monthly means of the reference data set with **L14** for precipitation, total runoff (baseflow and runoff), and evaporation.

    * Spatial maps comparing mean April 1 snow accumulation.

    * For selected large basins, comparison of the mean monthly time series of the water balance variables (no routing necessary, just sum over the basin using a basin mask). Also compare the anomaly time series in which each time series has been normalized with its own long-term mean.

## Control simulations for climate models

The control or historic simulations based on the climate model output will not have the same time signature as the historic dataset, but by construct should have the same climatology. Any comparisons of these simulations with the historic simulation should keep this in mind.

The same tests should be performed as for the reference dataset (see above), but the time series are not expected to show the same interannual variability.

Why is it complaining here?

* Additional checks:

    * Comparison of spatial maps of seasonal and annual variance of the water balance and energy variables with the reference dataset.


## Future climate simulations

The future climate simulations will show changes compared to the historic climate, which will make it impossible to directly compare to the reference dataset. However, the changes in the output should be consistent with changes in the forcings and all the sanity checks would still apply.

* Additional checks:

    * Anomaly between control simulation for the same model and the future climate simulation

    * Time series plots of water balance variables
