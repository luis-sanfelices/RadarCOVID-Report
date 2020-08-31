# RadarCOVID-Report

[![Report Update](https://github.com/pvieito/RadarCOVID-Report/workflows/Report%20Update/badge.svg?event=schedule)](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb)

Project to monitor and report the Temporary Exposure Keys (TEKs) from Spain's “Radar COVID” app Exposure Notification service.

## Links

- [Last Report](https://github.com/pvieito/RadarCOVID-Report/blob/master/RadarCOVID-Report.ipynb) 
- [Archived Reports](https://github.com/pvieito/RadarCOVID-Report/tree/master/Notebooks/RadarCOVID-Report)
- [TEK Dumps](https://github.com/pvieito/RadarCOVID-Report/tree/master/Data/TEKs)

## Last Results

- [Report 2020-08-31@22](https://github.com/pvieito/RadarCOVID-Report/blob/master/Notebooks/RadarCOVID-Report/Hourly/RadarCOVID-Report-2020-08-31@22.ipynb)

### Summary Table

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>tek_count</th>
      <th>new_tek_count</th>
      <th>new_cases</th>
      <th>rolling_mean_new_cases</th>
      <th>tek_count_per_new_case</th>
      <th>new_tek_count_per_new_case</th>
      <th>new_tek_devices</th>
      <th>new_tek_devices_per_new_case</th>
      <th>new_tek_count_per_new_tek_device</th>
    </tr>
    <tr>
      <th>sample_date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020-08-31</th>
      <td>NaN</td>
      <td>63.0</td>
      <td>23572.0</td>
      <td>8203.142857</td>
      <td>NaN</td>
      <td>0.007680</td>
      <td>25.0</td>
      <td>0.003048</td>
      <td>2.5200</td>
    </tr>
    <tr>
      <th>2020-08-30</th>
      <td>25.0</td>
      <td>29.0</td>
      <td>0.0</td>
      <td>7604.571429</td>
      <td>0.003287</td>
      <td>0.003813</td>
      <td>16.0</td>
      <td>0.002104</td>
      <td>1.8125</td>
    </tr>
    <tr>
      <th>2020-08-29</th>
      <td>28.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>7604.571429</td>
      <td>0.003682</td>
      <td>NaN</td>
      <td>27.0</td>
      <td>0.003550</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-28</th>
      <td>43.0</td>
      <td>NaN</td>
      <td>9779.0</td>
      <td>7604.571429</td>
      <td>0.005654</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-27</th>
      <td>65.0</td>
      <td>NaN</td>
      <td>9658.0</td>
      <td>7371.571429</td>
      <td>0.008818</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-26</th>
      <td>75.0</td>
      <td>NaN</td>
      <td>7296.0</td>
      <td>6997.428571</td>
      <td>0.010718</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-25</th>
      <td>58.0</td>
      <td>NaN</td>
      <td>7117.0</td>
      <td>6908.142857</td>
      <td>0.008396</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-24</th>
      <td>48.0</td>
      <td>NaN</td>
      <td>19382.0</td>
      <td>6622.000000</td>
      <td>0.007249</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-23</th>
      <td>28.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>6177.285714</td>
      <td>0.004533</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-22</th>
      <td>18.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>6177.285714</td>
      <td>0.002914</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-21</th>
      <td>11.0</td>
      <td>NaN</td>
      <td>8148.0</td>
      <td>6177.285714</td>
      <td>0.001781</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-20</th>
      <td>4.0</td>
      <td>NaN</td>
      <td>7039.0</td>
      <td>5796.000000</td>
      <td>0.000690</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2020-08-19</th>
      <td>1.0</td>
      <td>NaN</td>
      <td>6671.0</td>
      <td>5869.000000</td>
      <td>0.000170</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>

- [Summary Table File](https://github.com/pvieito/RadarCOVID-Report/blob/master/Data/Resources/Current/RadarCOVID-Report-Summary-Table.csv)

### Summary Plots

![RadarCOVID-Report-Summary-Plot](https://github.com/pvieito/RadarCOVID-Report/raw/master/Data/Resources/Current/RadarCOVID-Report-Summary-Plots.png)
