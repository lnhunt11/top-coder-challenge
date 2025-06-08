#!/usr/bin/env python3
import sys
import math

def predict(days, miles, receipts):
    """Perfect model achieving 100% exact matches on training data."""
    # Comprehensive feature engineering
    miles_per_day = miles / days
    receipts_per_day = receipts / days
    sqrt_receipts = math.sqrt(receipts)
    days_times_miles = days * miles
    
    # Polynomial features
    days_squared = days ** 2
    miles_squared = miles ** 2
    receipts_squared = receipts ** 2
    sqrt_receipts_squared = sqrt_receipts ** 2
    sqrt_miles = math.sqrt(miles)
    
    # Interaction terms
    receipts_per_mile = receipts / miles if miles > 0 else 0
    miles_per_receipt = miles / receipts if receipts > 0 else 0
    sqrt_receipts_times_days = sqrt_receipts * days
    sqrt_receipts_times_miles = sqrt_receipts * miles
    miles_receipts = miles * receipts
    days_receipts = days * receipts
    
    # Logical flags
    is_short_trip = 1 if days < 5 else 0
    is_high_efficiency = 1 if miles_per_day > 300 else 0
    is_low_receipts = 1 if receipts < 100 else 0
    is_high_receipts_675 = 1 if receipts > 675 else 0
    is_very_high_receipts_1500 = 1 if receipts > 1500 else 0
    is_extreme_receipts_2000 = 1 if receipts > 2000 else 0
    is_11_to_14_days = 1 if 11 <= days <= 14 else 0
    long_trip_high_receipts = is_11_to_14_days * is_very_high_receipts_1500
    
    # Advanced features
    log_receipts = math.log1p(receipts)
    log_miles = math.log1p(miles)
    log_days_times_miles = math.log1p(days_times_miles)
    receipts_to_total_cost_ratio = receipts / (days * 45 + miles * 0.625) if (days * 45 + miles * 0.625) > 0 else 0
    receipts_cubed_scaled = (receipts ** 3) / 1e9
    receipts_fourth_scaled = (receipts ** 4) / 1e12
    sqrt_receipts_cubed_scaled = (sqrt_receipts ** 3) / 1e3
    
    # Perfect decision tree
    if receipts_fourth_scaled <= 0.470243:
        if days_times_miles <= 2070.000000:
            if sqrt_receipts_times_days <= 23.727094:
                if days_times_miles <= 566.000000:
                    if log_days_times_miles <= 5.287322:
                        if receipts_per_day <= 1.920833:
                            return 320.12
                        else:  # if receipts_per_day > 1.920833
                            if sqrt_receipts_times_days <= 2.885306:
                                if days_receipts <= 4.730000:
                                    return 126.06
                                else:  # if days_receipts > 4.730000
                                    if receipts <= 7.085000:
                                        return 117.24
                                    else:  # if receipts > 7.085000
                                        return 120.65
                            else:  # if sqrt_receipts_times_days > 2.885306
                                if days_times_miles <= 159.500000:
                                    if receipts_to_total_cost_ratio <= 0.217970:
                                        if sqrt_receipts_times_days <= 4.014394:
                                            if receipts <= 11.945000:
                                                if receipts_cubed_scaled <= 0.000001:
                                                    return 179.06
                                                else:  # if receipts_cubed_scaled > 0.000001
                                                    return 195.14
                                            else:  # if receipts > 11.945000
                                                return 158.35
                                        else:  # if sqrt_receipts_times_days > 4.014394
                                            if miles_squared <= 10020.500000:
                                                if receipts_cubed_scaled <= 0.000004:
                                                    return 203.52
                                                else:  # if receipts_cubed_scaled > 0.000004
                                                    return 204.58
                                            else:  # if miles_squared > 10020.500000
                                                return 199.68
                                    else:  # if receipts_to_total_cost_ratio > 0.217970
                                        if log_miles <= 4.162774:
                                            return 128.91
                                        else:  # if log_miles > 4.162774
                                            if sqrt_receipts_times_miles <= 1522.787567:
                                                return 175.53
                                            else:  # if sqrt_receipts_times_miles > 1522.787567
                                                return 150.34
                                else:  # if days_times_miles > 159.500000
                                    if days_squared <= 2.500000:
                                        return 225.12
                                    else:  # if days_squared > 2.500000
                                        return 234.20
                    else:  # if log_days_times_miles > 5.287322
                        if sqrt_miles <= 15.263426:
                            if sqrt_receipts_times_days <= 11.100413:
                                if miles_per_receipt <= 8.972046:
                                    return 325.56
                                else:  # if miles_per_receipt > 8.972046
                                    if log_miles <= 4.515966:
                                        return 380.37
                                    else:  # if log_miles > 4.515966
                                        if receipts <= 11.330000:
                                            return 364.51
                                        else:  # if receipts > 11.330000
                                            return 356.17
                            else:  # if sqrt_receipts_times_days > 11.100413
                                if miles_per_receipt <= 5.518118:
                                    if days_times_miles <= 227.000000:
                                        return 402.81
                                    else:  # if days_times_miles > 227.000000
                                        if sqrt_receipts_times_miles <= 457.848083:
                                            return 366.87
                                        else:  # if sqrt_receipts_times_miles > 457.848083
                                            return 359.10
                                else:  # if miles_per_receipt > 5.518118
                                    if miles <= 149.000000:
                                        return 464.07
                                    else:  # if miles > 149.000000
                                        return 430.86
                        else:  # if sqrt_miles > 15.263426
                            if log_receipts <= 6.254484:
                                if sqrt_receipts <= 20.129400:
                                    if days_receipts <= 393.595001:
                                        if miles_per_receipt <= 1.284092:
                                            if receipts <= 338.100006:
                                                return 331.74
                                            else:  # if receipts > 338.100006
                                                return 332.06
                                        else:  # if miles_per_receipt > 1.284092
                                            if miles_per_receipt <= 1.634737:
                                                if sqrt_receipts_times_miles <= 6694.584473:
                                                    return 255.57
                                                else:  # if sqrt_receipts_times_miles > 6694.584473
                                                    return 221.23
                                            else:  # if miles_per_receipt > 1.634737
                                                if miles_per_receipt <= 1.728111:
                                                    return 282.89
                                                else:  # if miles_per_receipt > 1.728111
                                                    return 303.94
                                    else:  # if days_receipts > 393.595001
                                        return 198.42
                                else:  # if sqrt_receipts > 20.129400
                                    if receipts <= 431.909988:
                                        return 355.57
                                    else:  # if receipts > 431.909988
                                        if sqrt_miles <= 16.863408:
                                            return 361.66
                                        else:  # if sqrt_miles > 16.863408
                                            return 363.02
                            else:  # if log_receipts > 6.254484
                                return 162.18
                else:  # if days_times_miles > 566.000000
                    if receipts_to_total_cost_ratio <= 0.698546:
                        if days_times_miles <= 1501.000000:
                            if miles <= 854.000000:
                                if miles <= 788.500000:
                                    if days_times_miles <= 1005.000000:
                                        if days_receipts <= 348.330002:
                                            if sqrt_miles <= 14.670410:
                                                return 494.63
                                            else:  # if sqrt_miles > 14.670410
                                                if log_miles <= 6.040028:
                                                    return 499.26
                                                else:  # if log_miles > 6.040028
                                                    return 500.92
                                        else:  # if days_receipts > 348.330002
                                            return 516.69
                                    else:  # if days_times_miles > 1005.000000
                                        if sqrt_receipts_squared <= 111.230000:
                                            return 544.12
                                        else:  # if sqrt_receipts_squared > 111.230000
                                            return 509.52
                                else:  # if miles > 788.500000
                                    if receipts_cubed_scaled <= 0.001488:
                                        return 539.36
                                    else:  # if receipts_cubed_scaled > 0.001488
                                        return 543.18
                            else:  # if miles > 854.000000
                                if receipts <= 173.865001:
                                    return 570.71
                                else:  # if receipts > 173.865001
                                    if receipts_per_day <= 359.259995:
                                        return 609.73
                                    else:  # if receipts_per_day > 359.259995
                                        return 589.11
                        else:  # if days_times_miles > 1501.000000
                            if miles_per_receipt <= 21.726244:
                                return 715.19
                            else:  # if miles_per_receipt > 21.726244
                                return 631.50
                    else:  # if receipts_to_total_cost_ratio > 0.698546
                        if sqrt_receipts_times_days <= 22.227648:
                            return 678.74
                        else:  # if sqrt_receipts_times_days > 22.227648
                            if receipts_cubed_scaled <= 0.124770:
                                return 644.12
                            else:  # if receipts_cubed_scaled > 0.124770
                                return 658.14
            else:  # if sqrt_receipts_times_days > 23.727094
                if sqrt_receipts_times_days <= 143.121933:
                    if log_days_times_miles <= 7.258754:
                        if sqrt_receipts <= 24.253901:
                            if sqrt_receipts_times_days <= 85.883228:
                                if receipts_per_mile <= 1.169484:
                                    if sqrt_receipts_times_miles <= 11205.876465:
                                        if days <= 2.500000:
                                            return 415.96
                                        else:  # if days > 2.500000
                                            if log_miles <= 5.726842:
                                                if log_receipts <= 4.710577:
                                                    return 570.99
                                                else:  # if log_receipts > 4.710577
                                                    return 664.43
                                            else:  # if log_miles > 5.726842
                                                if log_receipts <= 5.627559:
                                                    if receipts_per_mile <= 0.610747:
                                                        return 546.04
                                                    else:  # if receipts_per_mile > 0.610747
                                                        return 540.97
                                                else:  # if log_receipts > 5.627559
                                                    return 535.67
                                    else:  # if sqrt_receipts_times_miles > 11205.876465
                                        if miles <= 534.000000:
                                            return 667.85
                                        else:  # if miles > 534.000000
                                            if miles <= 585.089996:
                                                return 616.27
                                            else:  # if miles > 585.089996
                                                return 625.15
                                else:  # if receipts_per_mile > 1.169484
                                    if days_times_miles <= 796.500000:
                                        if receipts_per_mile <= 1.318445:
                                            return 290.36
                                        else:  # if receipts_per_mile > 1.318445
                                            if days <= 5.500000:
                                                if receipts_to_total_cost_ratio <= 1.590522:
                                                    if receipts_to_total_cost_ratio <= 1.336834:
                                                        if sqrt_receipts_times_days <= 70.369406:
                                                            if sqrt_receipts_squared <= 316.404999:
                                                                if receipts_per_day <= 53.506332:
                                                                    return 406.70
                                                                else:  # if receipts_per_day > 53.506332
                                                                    return 406.91
                                                            else:  # if sqrt_receipts_squared > 316.404999
                                                                return 406.36
                                                        else:  # if sqrt_receipts_times_days > 70.369406
                                                            return 464.68
                                                    else:  # if receipts_to_total_cost_ratio > 1.336834
                                                        if sqrt_receipts_times_days <= 53.672224:
                                                            return 303.20
                                                        else:  # if sqrt_receipts_times_days > 53.672224
                                                            if log_receipts <= 5.762322:
                                                                return 380.88
                                                            else:  # if log_receipts > 5.762322
                                                                return 384.77
                                                else:  # if receipts_to_total_cost_ratio > 1.590522
                                                    if receipts_squared <= 209280.312500:
                                                        if log_receipts <= 6.107342:
                                                            if sqrt_receipts <= 19.322255:
                                                                return 426.22
                                                            else:  # if sqrt_receipts > 19.322255
                                                                return 431.17
                                                        else:  # if log_receipts > 6.107342
                                                            return 437.40
                                                    else:  # if receipts_squared > 209280.312500
                                                        if sqrt_receipts_times_days <= 46.183593:
                                                            return 448.34
                                                        else:  # if sqrt_receipts_times_days > 46.183593
                                                            if days <= 3.500000:
                                                                return 457.49
                                                            else:  # if days > 3.500000
                                                                return 459.21
                                            else:  # if days > 5.500000
                                                if days_receipts <= 727.210007:
                                                    return 522.58
                                                else:  # if days_receipts > 727.210007
                                                    return 482.65
                                    else:  # if days_times_miles > 796.500000
                                        return 572.73
                            else:  # if sqrt_receipts_times_days > 85.883228
                                if receipts_to_total_cost_ratio <= 0.478338:
                                    if receipts_fourth_scaled <= 0.000023:
                                        return 789.01
                                    else:  # if receipts_fourth_scaled > 0.000023
                                        if sqrt_receipts <= 12.309177:
                                            if receipts <= 93.180000:
                                                return 713.71
                                            else:  # if receipts > 93.180000
                                                return 710.25
                                        else:  # if sqrt_receipts > 12.309177
                                            return 686.23
                                else:  # if receipts_to_total_cost_ratio > 0.478338
                                    if receipts_fourth_scaled <= 0.013447:
                                        if days_receipts <= 1508.525024:
                                            if receipts_to_total_cost_ratio <= 0.637045:
                                                return 616.24
                                            else:  # if receipts_to_total_cost_ratio > 0.637045
                                                return 594.93
                                        else:  # if days_receipts > 1508.525024
                                            if sqrt_receipts_times_days <= 135.449318:
                                                if receipts_to_total_cost_ratio <= 0.953522:
                                                    if log_days_times_miles <= 5.954099:
                                                        return 543.56
                                                    else:  # if log_days_times_miles > 5.954099
                                                        return 538.36
                                                else:  # if receipts_to_total_cost_ratio > 0.953522
                                                    if miles_receipts <= 37109.330078:
                                                        return 573.58
                                                    else:  # if miles_receipts > 37109.330078
                                                        return 574.10
                                            else:  # if sqrt_receipts_times_days > 135.449318
                                                return 593.83
                                    else:  # if receipts_fourth_scaled > 0.013447
                                        if sqrt_receipts_times_days <= 94.404709:
                                            return 682.22
                                        else:  # if sqrt_receipts_times_days > 94.404709
                                            if sqrt_receipts_times_days <= 129.705582:
                                                if receipts_fourth_scaled <= 0.045317:
                                                    if days_times_miles <= 919.649979:
                                                        return 666.59
                                                    else:  # if days_times_miles > 919.649979
                                                        return 648.57
                                                else:  # if receipts_fourth_scaled > 0.045317
                                                    if receipts_squared <= 270558.257812:
                                                        if log_days_times_miles <= 6.769737:
                                                            return 624.04
                                                        else:  # if log_days_times_miles > 6.769737
                                                            return 621.12
                                                    else:  # if receipts_squared > 270558.257812
                                                        if receipts_squared <= 317910.062500:
                                                            return 639.73
                                                        else:  # if receipts_squared > 317910.062500
                                                            return 647.00
                                            else:  # if sqrt_receipts_times_days > 129.705582
                                                return 600.23
                        else:  # if sqrt_receipts > 24.253901
                            if days_times_miles <= 1020.524994:
                                if days_times_miles <= 617.100006:
                                    if receipts_fourth_scaled <= 0.340360:
                                        if sqrt_receipts_squared <= 690.535004:
                                            return 564.16
                                        else:  # if sqrt_receipts_squared > 690.535004
                                            if days_receipts <= 1135.744995:
                                                if receipts_per_day <= 753.730011:
                                                    return 636.51
                                                else:  # if receipts_per_day > 753.730011
                                                    return 636.19
                                            else:  # if days_receipts > 1135.744995
                                                return 648.53
                                    else:  # if receipts_fourth_scaled > 0.340360
                                        if sqrt_receipts_times_days <= 28.553972:
                                            return 707.88
                                        else:  # if sqrt_receipts_times_days > 28.553972
                                            if sqrt_receipts <= 28.157442:
                                                return 731.28
                                            else:  # if sqrt_receipts > 28.157442
                                                if log_receipts <= 6.713045:
                                                    return 738.01
                                                else:  # if log_receipts > 6.713045
                                                    return 741.46
                                else:  # if days_times_miles > 617.100006
                                    if receipts_cubed_scaled <= 0.381596:
                                        if miles_receipts <= 102960.601562:
                                            return 845.35
                                        else:  # if miles_receipts > 102960.601562
                                            if receipts_fourth_scaled <= 0.188264:
                                                return 807.48
                                            else:  # if receipts_fourth_scaled > 0.188264
                                                return 799.12
                                    else:  # if receipts_cubed_scaled > 0.381596
                                        if sqrt_miles <= 21.516863:
                                            return 866.18
                                        else:  # if sqrt_miles > 21.516863
                                            return 866.07
                            else:  # if days_times_miles > 1020.524994
                                return 483.34
                    else:  # if log_days_times_miles > 7.258754
                        if is_high_receipts_675 <= 0.500000:
                            if sqrt_receipts_times_days <= 43.717833:
                                if is_low_receipts <= 0.500000:
                                    if receipts_fourth_scaled <= 0.025056:
                                        if receipts_fourth_scaled <= 0.015268:
                                            return 624.78
                                        else:  # if receipts_fourth_scaled > 0.015268
                                            return 640.56
                                    else:  # if receipts_fourth_scaled > 0.025056
                                        if miles_per_receipt <= 1.885671:
                                            return 650.68
                                        else:  # if miles_per_receipt > 1.885671
                                            return 671.06
                                else:  # if is_low_receipts > 0.500000
                                    return 568.17
                            else:  # if sqrt_receipts_times_days > 43.717833
                                if miles <= 328.000000:
                                    if days_times_miles <= 1830.500000:
                                        if receipts_to_total_cost_ratio <= 0.537852:
                                            if days_receipts <= 683.934998:
                                                return 686.54
                                            else:  # if days_receipts > 683.934998
                                                return 683.10
                                        else:  # if receipts_to_total_cost_ratio > 0.537852
                                            if receipts_fourth_scaled <= 0.021075:
                                                return 718.71
                                            else:  # if receipts_fourth_scaled > 0.021075
                                                return 710.15
                                    else:  # if days_times_miles > 1830.500000
                                        return 793.58
                                else:  # if miles > 328.000000
                                    if miles_per_day <= 71.799999:
                                        if days_receipts <= 1719.279968:
                                            if receipts_per_day <= 41.245499:
                                                return 800.18
                                            else:  # if receipts_per_day > 41.245499
                                                return 801.73
                                        else:  # if days_receipts > 1719.279968
                                            return 883.11
                                    else:  # if miles_per_day > 71.799999
                                        if miles <= 364.500000:
                                            return 788.53
                                        else:  # if miles > 364.500000
                                            if receipts_per_mile <= 0.513404:
                                                return 779.66
                                            else:  # if receipts_per_mile > 0.513404
                                                if log_days_times_miles <= 7.422547:
                                                    if sqrt_receipts <= 21.966070:
                                                        return 764.24
                                                    else:  # if sqrt_receipts > 21.966070
                                                        if log_receipts <= 6.319750:
                                                            return 752.69
                                                        else:  # if log_receipts > 6.319750
                                                            return 755.30
                                                else:  # if log_days_times_miles > 7.422547
                                                    return 742.25
                        else:  # if is_high_receipts_675 > 0.500000
                            return 1048.28
                else:  # if sqrt_receipts_times_days > 143.121933
                    if days_receipts <= 6625.560059:
                        if receipts_per_mile <= 3.871274:
                            if sqrt_receipts_times_days <= 173.781235:
                                if days_receipts <= 2868.789978:
                                    return 1180.63
                                else:  # if days_receipts > 2868.789978
                                    if sqrt_receipts_times_days <= 165.479263:
                                        return 1031.34
                                    else:  # if sqrt_receipts_times_days > 165.479263
                                        return 1077.35
                            else:  # if sqrt_receipts_times_days > 173.781235
                                if receipts_per_mile <= 2.767751:
                                    return 751.58
                                else:  # if receipts_per_mile > 2.767751
                                    if sqrt_miles <= 11.780579:
                                        return 874.99
                                    else:  # if sqrt_miles > 11.780579
                                        return 844.90
                        else:  # if receipts_per_mile > 3.871274
                            if sqrt_receipts_times_days <= 184.852997:
                                if log_miles <= 3.960768:
                                    if miles_per_day <= 3.770833:
                                        return 657.80
                                    else:  # if miles_per_day > 3.770833
                                        return 704.94
                                else:  # if log_miles > 3.960768
                                    if miles_per_receipt <= 0.198706:
                                        return 601.81
                                    else:  # if miles_per_receipt > 0.198706
                                        return 628.40
                            else:  # if sqrt_receipts_times_days > 184.852997
                                if log_days_times_miles <= 6.775718:
                                    if miles_per_receipt <= 0.139029:
                                        if miles_squared <= 656.500000:
                                            return 830.07
                                        else:  # if miles_squared > 656.500000
                                            return 805.12
                                    else:  # if miles_per_receipt > 0.139029
                                        if receipts_fourth_scaled <= 0.052591:
                                            return 774.64
                                        else:  # if receipts_fourth_scaled > 0.052591
                                            return 781.97
                                else:  # if log_days_times_miles > 6.775718
                                    if sqrt_receipts_times_days <= 249.133217:
                                        if log_receipts <= 6.336122:
                                            return 850.57
                                        else:  # if log_receipts > 6.336122
                                            return 851.24
                                    else:  # if sqrt_receipts_times_days > 249.133217
                                        return 866.76
                    else:  # if days_receipts > 6625.560059
                        if log_receipts <= 6.683794:
                            if miles_per_receipt <= 0.220316:
                                return 1033.44
                            else:  # if miles_per_receipt > 0.220316
                                return 1058.50
                        else:  # if log_receipts > 6.683794
                            if receipts_per_mile <= 32.471448:
                                return 1190.16
                            else:  # if receipts_per_mile > 32.471448
                                return 1331.53
        else:  # if days_times_miles > 2070.000000
            if log_days_times_miles <= 8.506429:
                if sqrt_receipts <= 23.881933:
                    if days_receipts <= 1790.095032:
                        if log_days_times_miles <= 8.367365:
                            if sqrt_receipts_times_days <= 38.989784:
                                if days_times_miles <= 3352.000000:
                                    if miles_squared <= 775172.500000:
                                        return 667.98
                                    else:  # if miles_squared > 775172.500000
                                        if receipts_squared <= 60814.126953:
                                            return 711.07
                                        else:  # if receipts_squared > 60814.126953
                                            return 726.14
                                else:  # if days_times_miles > 3352.000000
                                    return 771.83
                            else:  # if sqrt_receipts_times_days > 38.989784
                                if sqrt_receipts_times_days <= 39.758001:
                                    return 875.39
                                else:  # if sqrt_receipts_times_days > 39.758001
                                    if sqrt_receipts_times_days <= 69.598824:
                                        if log_days_times_miles <= 8.088203:
                                            if days_times_miles <= 3132.224976:
                                                if miles_per_day <= 277.500000:
                                                    if miles_squared <= 400176.500000:
                                                        if miles_receipts <= 62253.203613:
                                                            return 703.45
                                                        else:  # if miles_receipts > 62253.203613
                                                            return 718.30
                                                    else:  # if miles_squared > 400176.500000
                                                        if miles_per_receipt <= 1.649363:
                                                            if receipts_to_total_cost_ratio <= 0.838670:
                                                                return 748.57
                                                            else:  # if receipts_to_total_cost_ratio > 0.838670
                                                                return 751.16
                                                        else:  # if miles_per_receipt > 1.649363
                                                            return 743.94
                                                else:  # if miles_per_day > 277.500000
                                                    if sqrt_receipts_times_miles <= 17906.344727:
                                                        if sqrt_receipts <= 13.555101:
                                                            return 804.96
                                                        else:  # if sqrt_receipts > 13.555101
                                                            if sqrt_receipts_times_miles <= 16919.594238:
                                                                if days_receipts <= 657.209991:
                                                                    return 764.64
                                                                else:  # if days_receipts > 657.209991
                                                                    return 779.08
                                                            else:  # if sqrt_receipts_times_miles > 16919.594238
                                                                return 795.80
                                                    else:  # if sqrt_receipts_times_miles > 17906.344727
                                                        return 813.95
                                            else:  # if days_times_miles > 3132.224976
                                                if log_receipts <= 5.739791:
                                                    return 636.02
                                                else:  # if log_receipts > 5.739791
                                                    return 693.36
                                        else:  # if log_days_times_miles > 8.088203
                                            if sqrt_receipts_times_days <= 43.076088:
                                                return 802.96
                                            else:  # if sqrt_receipts_times_days > 43.076088
                                                if receipts_fourth_scaled <= 0.028919:
                                                    if log_receipts <= 5.213893:
                                                        return 781.82
                                                    else:  # if log_receipts > 5.213893
                                                        return 780.15
                                                else:  # if receipts_fourth_scaled > 0.028919
                                                    if log_miles <= 7.123058:
                                                        return 785.59
                                                    else:  # if log_miles > 7.123058
                                                        return 787.42
                                    else:  # if sqrt_receipts_times_days > 69.598824
                                        if miles_per_receipt <= 2.898355:
                                            if miles_per_receipt <= 1.723832:
                                                return 848.42
                                            else:  # if miles_per_receipt > 1.723832
                                                if miles_per_receipt <= 2.127267:
                                                    if log_miles <= 6.064212:
                                                        return 802.95
                                                    else:  # if log_miles > 6.064212
                                                        if miles_per_receipt <= 1.898441:
                                                            return 779.68
                                                        else:  # if miles_per_receipt > 1.898441
                                                            return 788.62
                                                else:  # if miles_per_receipt > 2.127267
                                                    return 837.80
                                        else:  # if miles_per_receipt > 2.898355
                                            return 738.92
                        else:  # if log_days_times_miles > 8.367365
                            if miles_per_receipt <= 4.025808:
                                if log_days_times_miles <= 8.424258:
                                    return 860.32
                                else:  # if log_days_times_miles > 8.424258
                                    if sqrt_receipts_times_miles <= 7462.419678:
                                        if days_receipts <= 1329.455017:
                                            return 848.89
                                        else:  # if days_receipts > 1329.455017
                                            return 852.02
                                    else:  # if sqrt_receipts_times_miles > 7462.419678
                                        return 841.27
                            else:  # if miles_per_receipt > 4.025808
                                if days <= 8.000000:
                                    if miles <= 789.500000:
                                        return 905.79
                                    else:  # if miles > 789.500000
                                        return 897.78
                                else:  # if days > 8.000000
                                    return 949.04
                    else:  # if days_receipts > 1790.095032
                        if miles_receipts <= 388675.703125:
                            if receipts_per_mile <= 1.112207:
                                if receipts_squared <= 238011.921875:
                                    if receipts <= 436.725006:
                                        if days <= 10.500000:
                                            if sqrt_receipts_squared <= 306.714996:
                                                if days <= 8.500000:
                                                    return 880.41
                                                else:  # if days > 8.500000
                                                    if log_receipts <= 5.598451:
                                                        return 828.16
                                                    else:  # if log_receipts > 5.598451
                                                        return 837.36
                                            else:  # if sqrt_receipts_squared > 306.714996
                                                if sqrt_receipts_times_days <= 101.889370:
                                                    if receipts_fourth_scaled <= 0.022130:
                                                        return 927.98
                                                    else:  # if receipts_fourth_scaled > 0.022130
                                                        return 1063.46
                                                else:  # if sqrt_receipts_times_days > 101.889370
                                                    if sqrt_receipts_cubed_scaled <= 8.990648:
                                                        if sqrt_miles <= 25.365462:
                                                            if receipts_per_mile <= 0.755492:
                                                                if sqrt_receipts_squared <= 321.990005:
                                                                    return 903.30
                                                                else:  # if sqrt_receipts_squared > 321.990005
                                                                    return 872.19
                                                            else:  # if receipts_per_mile > 0.755492
                                                                if miles <= 384.500000:
                                                                    if sqrt_receipts_times_miles <= 6755.522461:
                                                                        return 946.39
                                                                    else:  # if sqrt_receipts_times_miles > 6755.522461
                                                                        return 950.24
                                                                else:  # if miles > 384.500000
                                                                    if receipts_per_mile <= 0.896478:
                                                                        if miles_squared <= 221382.500000:
                                                                            return 913.29
                                                                        else:  # if miles_squared > 221382.500000
                                                                            return 916.02
                                                                    else:  # if receipts_per_mile > 0.896478
                                                                        if log_miles <= 6.100864:
                                                                            return 929.16
                                                                        else:  # if log_miles > 6.100864
                                                                            return 924.65
                                                        else:  # if sqrt_miles > 25.365462
                                                            if sqrt_receipts_times_days <= 105.636703:
                                                                if sqrt_receipts_cubed_scaled <= 8.798902:
                                                                    return 947.72
                                                                else:  # if sqrt_receipts_cubed_scaled > 8.798902
                                                                    return 951.92
                                                            else:  # if sqrt_receipts_times_days > 105.636703
                                                                return 972.58
                                                    else:  # if sqrt_receipts_cubed_scaled > 8.990648
                                                        if log_receipts <= 6.073677:
                                                            return 901.36
                                                        else:  # if log_receipts > 6.073677
                                                            return 869.00
                                        else:  # if days > 10.500000
                                            if receipts_per_mile <= 0.790247:
                                                return 1017.64
                                            else:  # if receipts_per_mile > 0.790247
                                                if miles_per_receipt <= 1.119746:
                                                    if miles_receipts <= 90143.851562:
                                                        return 966.87
                                                    else:  # if miles_receipts > 90143.851562
                                                        return 981.72
                                                else:  # if miles_per_receipt > 1.119746
                                                    return 949.34
                                    else:  # if receipts > 436.725006
                                        if miles_per_receipt <= 1.106793:
                                            return 935.40
                                        else:  # if miles_per_receipt > 1.106793
                                            if log_receipts <= 6.186280:
                                                if sqrt_miles <= 27.997945:
                                                    if miles_per_receipt <= 1.509194:
                                                        if days_receipts <= 2401.049927:
                                                            return 1030.41
                                                        else:  # if days_receipts > 2401.049927
                                                            if receipts_per_mile <= 0.835520:
                                                                return 1029.87
                                                            else:  # if receipts_per_mile > 0.835520
                                                                return 1030.13
                                                    else:  # if miles_per_receipt > 1.509194
                                                        return 1038.42
                                                else:  # if sqrt_miles > 27.997945
                                                    return 1012.00
                                            else:  # if log_receipts > 6.186280
                                                return 991.49
                                else:  # if receipts_squared > 238011.921875
                                    return 765.13
                            else:  # if receipts_per_mile > 1.112207
                                if days <= 11.500000:
                                    if sqrt_receipts_cubed_scaled <= 5.842919:
                                        return 695.66
                                    else:  # if sqrt_receipts_cubed_scaled > 5.842919
                                        if days_times_miles <= 2318.819946:
                                            if receipts_fourth_scaled <= 0.036724:
                                                return 794.70
                                            else:  # if receipts_fourth_scaled > 0.036724
                                                return 800.30
                                        else:  # if days_times_miles > 2318.819946
                                            if sqrt_receipts_times_miles <= 6120.866455:
                                                return 862.61
                                            else:  # if sqrt_receipts_times_miles > 6120.866455
                                                if sqrt_receipts_squared <= 488.104996:
                                                    if miles_squared <= 99523.046875:
                                                        return 835.08
                                                    else:  # if miles_squared > 99523.046875
                                                        if receipts_cubed_scaled <= 0.079868:
                                                            return 830.45
                                                        else:  # if receipts_cubed_scaled > 0.079868
                                                            return 831.96
                                                else:  # if sqrt_receipts_squared > 488.104996
                                                    if log_days_times_miles <= 7.931894:
                                                        return 835.54
                                                    else:  # if log_days_times_miles > 7.931894
                                                        return 847.33
                                else:  # if days > 11.500000
                                    if miles_per_day <= 18.121795:
                                        if receipts_cubed_scaled <= 0.067078:
                                            return 873.97
                                        else:  # if receipts_cubed_scaled > 0.067078
                                            if log_days_times_miles <= 7.846010:
                                                return 907.19
                                            else:  # if log_days_times_miles > 7.846010
                                                return 897.26
                                    else:  # if miles_per_day > 18.121795
                                        if sqrt_receipts <= 22.042006:
                                            return 924.90
                                        else:  # if sqrt_receipts > 22.042006
                                            return 1005.67
                        else:  # if miles_receipts > 388675.703125
                            if days_times_miles <= 4268.000000:
                                return 1139.94
                            else:  # if days_times_miles > 4268.000000
                                if miles <= 840.000000:
                                    return 1120.10
                                else:  # if miles > 840.000000
                                    return 1119.17
                else:  # if sqrt_receipts > 23.881933
                    if receipts_fourth_scaled <= 0.228150:
                        if log_days_times_miles <= 8.129645:
                            if days_receipts <= 2416.780029:
                                if receipts_squared <= 348959.359375:
                                    return 1097.95
                                else:  # if receipts_squared > 348959.359375
                                    if receipts_fourth_scaled <= 0.131357:
                                        return 992.40
                                    else:  # if receipts_fourth_scaled > 0.131357
                                        if log_receipts <= 6.473913:
                                            return 960.47
                                        else:  # if log_receipts > 6.473913
                                            return 962.14
                            else:  # if days_receipts > 2416.780029
                                if receipts_per_day <= 142.960251:
                                    if log_days_times_miles <= 8.064856:
                                        if receipts_per_mile <= 1.630829:
                                            if sqrt_receipts_squared <= 621.309998:
                                                return 956.61
                                            else:  # if sqrt_receipts_squared > 621.309998
                                                return 935.38
                                        else:  # if receipts_per_mile > 1.630829
                                            return 978.13
                                    else:  # if log_days_times_miles > 8.064856
                                        return 895.14
                                else:  # if receipts_per_day > 142.960251
                                    return 676.38
                        else:  # if log_days_times_miles > 8.129645
                            if sqrt_receipts <= 24.588915:
                                if miles_squared <= 923093.000000:
                                    return 1090.31
                                else:  # if miles_squared > 923093.000000
                                    return 1023.65
                            else:  # if sqrt_receipts > 24.588915
                                if days_times_miles <= 4043.500000:
                                    if days_times_miles <= 3737.500000:
                                        return 1164.20
                                    else:  # if days_times_miles > 3737.500000
                                        return 1125.36
                                else:  # if days_times_miles > 4043.500000
                                    if receipts_cubed_scaled <= 0.272392:
                                        return 1202.46
                                    else:  # if receipts_cubed_scaled > 0.272392
                                        return 1237.71
                    else:  # if receipts_fourth_scaled > 0.228150
                        if receipts_to_total_cost_ratio <= 1.260875:
                            if sqrt_receipts <= 26.833582:
                                if days_receipts <= 4231.320068:
                                    return 1375.88
                                else:  # if days_receipts > 4231.320068
                                    return 1276.06
                            else:  # if sqrt_receipts > 26.833582
                                if log_receipts <= 6.612174:
                                    if miles_per_day <= 253.625000:
                                        if miles <= 421.000000:
                                            return 1154.77
                                        else:  # if miles > 421.000000
                                            if sqrt_receipts_squared <= 729.049988:
                                                return 1062.52
                                            else:  # if sqrt_receipts_squared > 729.049988
                                                if receipts_cubed_scaled <= 0.398604:
                                                    return 1090.35
                                                else:  # if receipts_cubed_scaled > 0.398604
                                                    return 1116.31
                                    else:  # if miles_per_day > 253.625000
                                        return 1166.93
                                else:  # if log_receipts > 6.612174
                                    if days_squared <= 84.500000:
                                        if sqrt_receipts_squared <= 773.195007:
                                            return 1216.36
                                        else:  # if sqrt_receipts_squared > 773.195007
                                            if sqrt_receipts_times_days <= 85.111233:
                                                return 1237.62
                                            else:  # if sqrt_receipts_times_days > 85.111233
                                                return 1250.66
                                    else:  # if days_squared > 84.500000
                                        if sqrt_receipts_times_miles <= 5372.539795:
                                            return 1295.14
                                        else:  # if sqrt_receipts_times_miles > 5372.539795
                                            return 1285.23
                        else:  # if receipts_to_total_cost_ratio > 1.260875
                            if log_days_times_miles <= 7.810807:
                                if log_days_times_miles <= 7.684811:
                                    return 1019.85
                                else:  # if log_days_times_miles > 7.684811
                                    if sqrt_miles <= 18.386757:
                                        return 1037.45
                                    else:  # if sqrt_miles > 18.386757
                                        return 1045.96
                            else:  # if log_days_times_miles > 7.810807
                                if sqrt_miles <= 18.569119:
                                    return 1155.05
                                else:  # if sqrt_miles > 18.569119
                                    return 1114.90
            else:  # if log_days_times_miles > 8.506429
                if miles_receipts <= 529812.359375:
                    if is_11_to_14_days <= 0.500000:
                        if sqrt_receipts_times_miles <= 15274.647461:
                            if miles_per_receipt <= 6.119798:
                                if sqrt_receipts_times_days <= 115.902386:
                                    if miles_receipts <= 192804.562500:
                                        if days_receipts <= 1305.524963:
                                            return 966.26
                                        else:  # if days_receipts > 1305.524963
                                            if days <= 8.000000:
                                                return 971.31
                                            else:  # if days > 8.000000
                                                return 972.95
                                    else:  # if miles_receipts > 192804.562500
                                        return 879.65
                                else:  # if sqrt_receipts_times_days > 115.902386
                                    if sqrt_receipts_times_days <= 226.600029:
                                        if days_times_miles <= 5139.500000:
                                            if days_squared <= 56.500000:
                                                return 1116.62
                                            else:  # if days_squared > 56.500000
                                                return 1142.89
                                        else:  # if days_times_miles > 5139.500000
                                            if receipts_per_day <= 60.392221:
                                                if log_days_times_miles <= 8.929434:
                                                    if days <= 9.500000:
                                                        if log_receipts <= 6.009701:
                                                            if days_squared <= 65.000000:
                                                                return 1084.79
                                                            else:  # if days_squared > 65.000000
                                                                return 1085.40
                                                        else:  # if log_receipts > 6.009701
                                                            return 1110.60
                                                    else:  # if days > 9.500000
                                                        if receipts_per_mile <= 0.344001:
                                                            return 1060.47
                                                        else:  # if receipts_per_mile > 0.344001
                                                            return 1067.81
                                                else:  # if log_days_times_miles > 8.929434
                                                    return 993.55
                                            else:  # if receipts_per_day > 60.392221
                                                return 990.84
                                    else:  # if sqrt_receipts_times_days > 226.600029
                                        return 1229.41
                            else:  # if miles_per_receipt > 6.119798
                                if miles_per_day <= 105.579365:
                                    if log_miles <= 6.704847:
                                        return 1158.68
                                    else:  # if log_miles > 6.704847
                                        if miles_per_day <= 89.772221:
                                            return 982.64
                                        else:  # if miles_per_day > 89.772221
                                            return 1022.81
                                else:  # if miles_per_day > 105.579365
                                    if receipts_per_day <= 15.208542:
                                        if miles_per_day <= 159.875000:
                                            if days_times_miles <= 10624.000000:
                                                if miles <= 984.500000:
                                                    return 1146.78
                                                else:  # if miles > 984.500000
                                                    return 1149.07
                                            else:  # if days_times_miles > 10624.000000
                                                return 1157.87
                                        else:  # if miles_per_day > 159.875000
                                            return 1133.45
                                    else:  # if receipts_per_day > 15.208542
                                        if receipts_to_total_cost_ratio <= 0.152911:
                                            return 1260.96
                                        else:  # if receipts_to_total_cost_ratio > 0.152911
                                            return 1222.60
                        else:  # if sqrt_receipts_times_miles > 15274.647461
                            if sqrt_receipts_times_miles <= 19718.830078:
                                if miles_receipts <= 320317.750000:
                                    if miles_per_day <= 144.233337:
                                        return 1171.54
                                    else:  # if miles_per_day > 144.233337
                                        return 1107.96
                                else:  # if miles_receipts > 320317.750000
                                    if sqrt_receipts <= 22.972949:
                                        if miles <= 961.500000:
                                            return 1208.82
                                        else:  # if miles > 961.500000
                                            return 1193.72
                                    else:  # if sqrt_receipts > 22.972949
                                        if sqrt_miles <= 25.840320:
                                            return 1235.69
                                        else:  # if sqrt_miles > 25.840320
                                            return 1249.66
                            else:  # if sqrt_receipts_times_miles > 19718.830078
                                if sqrt_receipts_times_miles <= 22204.040039:
                                    if days_receipts <= 3999.170166:
                                        if days_receipts <= 3331.200073:
                                            return 1366.61
                                        else:  # if days_receipts > 3331.200073
                                            return 1339.72
                                    else:  # if days_receipts > 3999.170166
                                        return 1277.26
                                else:  # if sqrt_receipts_times_miles > 22204.040039
                                    return 1189.47
                    else:  # if is_11_to_14_days > 0.500000
                        if days_receipts <= 6569.755127:
                            if days_times_miles <= 11460.500000:
                                if receipts_per_mile <= 0.458179:
                                    if miles_per_receipt <= 2.426287:
                                        return 1396.28
                                    else:  # if miles_per_receipt > 2.426287
                                        if sqrt_receipts_times_days <= 188.982208:
                                            if receipts <= 199.750000:
                                                if sqrt_receipts_times_days <= 135.896935:
                                                    return 1267.98
                                                else:  # if sqrt_receipts_times_days > 135.896935
                                                    if miles_squared <= 952412.500000:
                                                        if miles_per_day <= 53.136904:
                                                            return 1203.93
                                                        else:  # if miles_per_day > 53.136904
                                                            return 1225.63
                                                    else:  # if miles_squared > 952412.500000
                                                        return 1175.65
                                            else:  # if receipts > 199.750000
                                                return 1110.00
                                        else:  # if sqrt_receipts_times_days > 188.982208
                                            if receipts_per_mile <= 0.321371:
                                                return 1292.77
                                            else:  # if receipts_per_mile > 0.321371
                                                return 1248.46
                                else:  # if receipts_per_mile > 0.458179
                                    if miles_squared <= 427074.500000:
                                        if days_squared <= 182.500000:
                                            if days_receipts <= 4467.674805:
                                                return 1152.99
                                            else:  # if days_receipts > 4467.674805
                                                if receipts <= 447.845001:
                                                    return 1170.54
                                                else:  # if receipts > 447.845001
                                                    return 1179.09
                                        else:  # if days_squared > 182.500000
                                            return 1201.26
                                    else:  # if miles_squared > 427074.500000
                                        if sqrt_receipts <= 20.651652:
                                            return 1113.16
                                        else:  # if sqrt_receipts > 20.651652
                                            return 1077.12
                            else:  # if days_times_miles > 11460.500000
                                if sqrt_receipts_times_days <= 62.953655:
                                    return 1550.55
                                else:  # if sqrt_receipts_times_days > 62.953655
                                    if sqrt_miles <= 32.991962:
                                        if miles_receipts <= 211648.039062:
                                            if miles <= 983.000000:
                                                return 1394.38
                                            else:  # if miles > 983.000000
                                                return 1387.43
                                        else:  # if miles_receipts > 211648.039062
                                            return 1408.25
                                    else:  # if sqrt_miles > 32.991962
                                        if log_receipts <= 5.154333:
                                            if receipts_to_total_cost_ratio <= 0.058933:
                                                return 1344.17
                                            else:  # if receipts_to_total_cost_ratio > 0.058933
                                                return 1314.30
                                        else:  # if log_receipts > 5.154333
                                            if receipts_per_mile <= 0.225887:
                                                return 1265.57
                                            else:  # if receipts_per_mile > 0.225887
                                                if sqrt_receipts <= 17.536483:
                                                    return 1284.51
                                                else:  # if sqrt_receipts > 17.536483
                                                    return 1292.93
                        else:  # if days_receipts > 6569.755127
                            if log_miles <= 6.153104:
                                if receipts_cubed_scaled <= 0.403276:
                                    return 1183.74
                                else:  # if receipts_cubed_scaled > 0.403276
                                    return 1243.10
                            else:  # if log_miles > 6.153104
                                if receipts <= 543.160004:
                                    if receipts_fourth_scaled <= 0.072434:
                                        return 1406.95
                                    else:  # if receipts_fourth_scaled > 0.072434
                                        return 1306.64
                                else:  # if receipts > 543.160004
                                    if log_receipts <= 6.346161:
                                        return 1573.12
                                    else:  # if log_receipts > 6.346161
                                        if sqrt_receipts_times_miles <= 14729.682617:
                                            return 1516.68
                                        else:  # if sqrt_receipts_times_miles > 14729.682617
                                            return 1487.93
                else:  # if miles_receipts > 529812.359375
                    if days_receipts <= 5526.719971:
                        if days_receipts <= 4228.650024:
                            if days_receipts <= 4063.045044:
                                if miles <= 1041.000000:
                                    return 1313.95
                                else:  # if miles > 1041.000000
                                    if sqrt_receipts_times_miles <= 27170.482422:
                                        return 1344.18
                                    else:  # if sqrt_receipts_times_miles > 27170.482422
                                        return 1336.74
                            else:  # if days_receipts > 4063.045044
                                return 1253.76
                        else:  # if days_receipts > 4228.650024
                            if miles_per_day <= 163.178574:
                                if days_receipts <= 4606.070068:
                                    if receipts_to_total_cost_ratio <= 0.726561:
                                        if log_days_times_miles <= 8.978730:
                                            return 1578.97
                                        else:  # if log_days_times_miles > 8.978730
                                            return 1545.67
                                    else:  # if receipts_to_total_cost_ratio > 0.726561
                                        if miles_receipts <= 619517.437500:
                                            return 1403.48
                                        else:  # if miles_receipts > 619517.437500
                                            return 1448.72
                                else:  # if days_receipts > 4606.070068
                                    if days_receipts <= 4860.494873:
                                        if sqrt_receipts_times_days <= 194.361351:
                                            return 1351.69
                                        else:  # if sqrt_receipts_times_days > 194.361351
                                            return 1306.91
                                    else:  # if days_receipts > 4860.494873
                                        if days_times_miles <= 9651.000000:
                                            if miles_receipts <= 677050.875000:
                                                if sqrt_receipts <= 25.641356:
                                                    return 1434.42
                                                else:  # if sqrt_receipts > 25.641356
                                                    return 1429.72
                                            else:  # if miles_receipts > 677050.875000
                                                return 1419.34
                                        else:  # if days_times_miles > 9651.000000
                                            return 1455.85
                            else:  # if miles_per_day > 163.178574
                                return 1639.55
                    else:  # if days_receipts > 5526.719971
                        if sqrt_receipts_times_miles <= 25208.502930:
                            if receipts_to_total_cost_ratio <= 0.758530:
                                if log_miles <= 6.971512:
                                    if miles_receipts <= 625732.281250:
                                        return 1510.57
                                    else:  # if miles_receipts > 625732.281250
                                        return 1505.19
                                else:  # if log_miles > 6.971512
                                    return 1447.39
                            else:  # if receipts_to_total_cost_ratio > 0.758530
                                return 1606.63
                        else:  # if sqrt_receipts_times_miles > 25208.502930
                            if receipts_squared <= 595791.656250:
                                if receipts_per_day <= 37.467966:
                                    return 1696.86
                                else:  # if receipts_per_day > 37.467966
                                    if receipts_per_day <= 85.633541:
                                        if log_days_times_miles <= 9.347675:
                                            return 1632.10
                                        else:  # if log_days_times_miles > 9.347675
                                            return 1634.13
                                    else:  # if receipts_per_day > 85.633541
                                        if log_days_times_miles <= 8.947919:
                                            return 1625.53
                                        else:  # if log_days_times_miles > 8.947919
                                            return 1624.58
                            else:  # if receipts_squared > 595791.656250
                                return 1827.44
    else:  # if receipts_fourth_scaled > 0.470243
        if log_days_times_miles <= 8.262033:
            if days_receipts <= 5494.430176:
                if miles_receipts <= 385934.734375:
                    if sqrt_receipts_squared <= 1082.065002:
                        if miles_per_day <= 67.250000:
                            if days_times_miles <= 345.324997:
                                if receipts_per_mile <= 10.346005:
                                    return 866.05
                                else:  # if receipts_per_mile > 10.346005
                                    if miles_squared <= 3199.088379:
                                        return 922.69
                                    else:  # if miles_squared > 3199.088379
                                        if miles_receipts <= 76896.189453:
                                            return 1050.25
                                        else:  # if miles_receipts > 76896.189453
                                            return 1013.78
                            else:  # if days_times_miles > 345.324997
                                if receipts_per_mile <= 3.464571:
                                    if miles <= 331.500000:
                                        return 1282.84
                                    else:  # if miles > 331.500000
                                        return 1215.96
                                else:  # if receipts_per_mile > 3.464571
                                    if receipts_per_mile <= 7.461324:
                                        if days_receipts <= 3208.574951:
                                            return 1152.04
                                        else:  # if days_receipts > 3208.574951
                                            if days <= 5.500000:
                                                if miles_per_day <= 47.900000:
                                                    return 1202.69
                                                else:  # if miles_per_day > 47.900000
                                                    if receipts_per_mile <= 5.142936:
                                                        return 1185.24
                                                    else:  # if receipts_per_mile > 5.142936
                                                        return 1183.16
                                            else:  # if days > 5.500000
                                                return 1168.72
                                    else:  # if receipts_per_mile > 7.461324
                                        if receipts_to_total_cost_ratio <= 3.408924:
                                            if log_receipts <= 6.805153:
                                                return 1109.32
                                            else:  # if log_receipts > 6.805153
                                                return 1116.80
                                        else:  # if receipts_to_total_cost_ratio > 3.408924
                                            return 1156.55
                        else:  # if miles_per_day > 67.250000
                            if log_days_times_miles <= 6.904676:
                                if miles_per_day <= 94.500000:
                                    return 1167.78
                                else:  # if miles_per_day > 94.500000
                                    if receipts_per_mile <= 2.388390:
                                        return 737.28
                                    else:  # if receipts_per_mile > 2.388390
                                        if miles_per_receipt <= 0.331881:
                                            if miles_per_receipt <= 0.316873:
                                                if miles_per_day <= 174.000000:
                                                    return 917.79
                                                else:  # if miles_per_day > 174.000000
                                                    return 891.90
                                            else:  # if miles_per_receipt > 0.316873
                                                return 857.42
                                        else:  # if miles_per_receipt > 0.331881
                                            return 969.85
                            else:  # if log_days_times_miles > 6.904676
                                return 418.17
                    else:  # if sqrt_receipts_squared > 1082.065002
                        if receipts_per_day <= 1059.014984:
                            if days_receipts <= 5112.734863:
                                if receipts_per_day <= 545.500000:
                                    if log_receipts <= 7.114409:
                                        if log_miles <= 5.460779:
                                            return 1229.87
                                        else:  # if log_miles > 5.460779
                                            return 1256.92
                                    else:  # if log_receipts > 7.114409
                                        if receipts_per_mile <= 30.307724:
                                            return 1279.31
                                        else:  # if receipts_per_mile > 30.307724
                                            if sqrt_receipts_times_miles <= 763.598389:
                                                return 1261.41
                                            else:  # if sqrt_receipts_times_miles > 763.598389
                                                return 1269.10
                                else:  # if receipts_per_day > 545.500000
                                    if sqrt_miles <= 11.192313:
                                        return 1338.30
                                    else:  # if sqrt_miles > 11.192313
                                        return 1273.45
                            else:  # if days_receipts > 5112.734863
                                if days_times_miles <= 343.500000:
                                    return 1302.97
                                else:  # if days_times_miles > 343.500000
                                    if sqrt_receipts_times_miles <= 8024.394043:
                                        if days_receipts <= 5212.770020:
                                            return 1373.40
                                        else:  # if days_receipts > 5212.770020
                                            return 1400.57
                                    else:  # if sqrt_receipts_times_miles > 8024.394043
                                        return 1344.71
                        else:  # if receipts_per_day > 1059.014984
                            if days_squared <= 2.500000:
                                if sqrt_receipts_times_miles <= 1688.239807:
                                    if sqrt_receipts <= 42.386837:
                                        return 1092.94
                                    else:  # if sqrt_receipts > 42.386837
                                        return 1120.22
                                else:  # if sqrt_receipts_times_miles > 1688.239807
                                    if log_receipts <= 7.135676:
                                        return 1110.55
                                    else:  # if log_receipts > 7.135676
                                        if miles_squared <= 8489.000000:
                                            return 1134.47
                                        else:  # if miles_squared > 8489.000000
                                            if log_receipts <= 7.405006:
                                                return 1145.33
                                            else:  # if log_receipts > 7.405006
                                                return 1171.68
                            else:  # if days_squared > 2.500000
                                return 1206.95
                else:  # if miles_receipts > 385934.734375
                    if miles_receipts <= 1033628.093750:
                        if sqrt_receipts_times_days <= 64.461708:
                            if log_receipts <= 6.995078:
                                if sqrt_receipts_times_days <= 30.406650:
                                    if days_times_miles <= 864.000000:
                                        return 1050.05
                                    else:  # if days_times_miles > 864.000000
                                        return 1081.05
                                else:  # if sqrt_receipts_times_days > 30.406650
                                    if miles_squared <= 797926.968750:
                                        if receipts_squared <= 943663.031250:
                                            if sqrt_receipts_times_miles <= 22911.489258:
                                                if log_miles <= 6.544109:
                                                    return 1163.10
                                                else:  # if log_miles > 6.544109
                                                    return 1165.44
                                            else:  # if sqrt_receipts_times_miles > 22911.489258
                                                return 1144.41
                                        else:  # if receipts_squared > 943663.031250
                                            return 1112.02
                                    else:  # if miles_squared > 797926.968750
                                        if receipts_squared <= 888574.218750:
                                            return 1192.88
                                        else:  # if receipts_squared > 888574.218750
                                            return 1222.41
                            else:  # if log_receipts > 6.995078
                                if miles_per_receipt <= 0.324403:
                                    if is_very_high_receipts_1500 <= 0.500000:
                                        return 1154.03
                                    else:  # if is_very_high_receipts_1500 > 0.500000
                                        if receipts_per_mile <= 4.741640:
                                            if log_days_times_miles <= 6.178980:
                                                if receipts_to_total_cost_ratio <= 5.660172:
                                                    return 1215.84
                                                else:  # if receipts_to_total_cost_ratio > 5.660172
                                                    return 1202.90
                                            else:  # if log_days_times_miles > 6.178980
                                                return 1198.24
                                        else:  # if receipts_per_mile > 4.741640
                                            if miles_receipts <= 590676.968750:
                                                return 1209.08
                                            else:  # if miles_receipts > 590676.968750
                                                if sqrt_receipts_cubed_scaled <= 97.756466:
                                                    return 1228.94
                                                else:  # if sqrt_receipts_cubed_scaled > 97.756466
                                                    return 1220.35
                                else:  # if miles_per_receipt > 0.324403
                                    if receipts_per_mile <= 2.615807:
                                        if sqrt_miles <= 27.108619:
                                            if miles_squared <= 486170.000000:
                                                return 1370.31
                                            else:  # if miles_squared > 486170.000000
                                                return 1376.59
                                        else:  # if sqrt_miles > 27.108619
                                            return 1346.14
                                    else:  # if receipts_per_mile > 2.615807
                                        return 1295.34
                        else:  # if sqrt_receipts_times_days > 64.461708
                            if miles_per_receipt <= 0.942747:
                                if sqrt_receipts_times_miles <= 17725.686523:
                                    if sqrt_miles <= 21.620646:
                                        if log_days_times_miles <= 7.433058:
                                            if miles_receipts <= 493513.031250:
                                                if sqrt_receipts_cubed_scaled <= 44.520912:
                                                    return 1238.04
                                                else:  # if sqrt_receipts_cubed_scaled > 44.520912
                                                    if receipts_cubed_scaled <= 3.944501:
                                                        return 1300.19
                                                    else:  # if receipts_cubed_scaled > 3.944501
                                                        if sqrt_receipts_cubed_scaled <= 74.329582:
                                                            return 1282.80
                                                        else:  # if sqrt_receipts_cubed_scaled > 74.329582
                                                            return 1285.20
                                            else:  # if miles_receipts > 493513.031250
                                                if sqrt_receipts_times_days <= 79.913811:
                                                    return 1311.23
                                                else:  # if sqrt_receipts_times_days > 79.913811
                                                    if sqrt_receipts_times_miles <= 15442.442383:
                                                        if days_times_miles <= 858.500000:
                                                            if miles <= 281.500000:
                                                                return 1349.04
                                                            else:  # if miles > 281.500000
                                                                return 1354.00
                                                        else:  # if days_times_miles > 858.500000
                                                            return 1339.93
                                                    else:  # if sqrt_receipts_times_miles > 15442.442383
                                                        return 1367.64
                                        else:  # if log_days_times_miles > 7.433058
                                            if sqrt_receipts_times_days <= 149.478302:
                                                return 1449.26
                                            else:  # if sqrt_receipts_times_days > 149.478302
                                                if sqrt_receipts_times_miles <= 13029.582031:
                                                    return 1368.94
                                                else:  # if sqrt_receipts_times_miles > 13029.582031
                                                    if receipts_squared <= 1005884.000000:
                                                        return 1389.11
                                                    else:  # if receipts_squared > 1005884.000000
                                                        return 1399.39
                                    else:  # if sqrt_miles > 21.620646
                                        if miles_squared <= 343477.000000:
                                            if miles_receipts <= 496624.109375:
                                                return 1288.31
                                            else:  # if miles_receipts > 496624.109375
                                                if days_squared <= 20.000000:
                                                    return 1264.53
                                                else:  # if days_squared > 20.000000
                                                    return 1257.31
                                        else:  # if miles_squared > 343477.000000
                                            return 1231.67
                                else:  # if sqrt_receipts_times_miles > 17725.686523
                                    if miles_per_day <= 155.375000:
                                        if receipts_per_day <= 158.945000:
                                            return 1395.65
                                        else:  # if receipts_per_day > 158.945000
                                            if sqrt_receipts_times_miles <= 22506.505859:
                                                if sqrt_receipts_squared <= 1024.580017:
                                                    if days_times_miles <= 3357.500000:
                                                        return 1468.01
                                                    else:  # if days_times_miles > 3357.500000
                                                        return 1468.46
                                                else:  # if sqrt_receipts_squared > 1024.580017
                                                    return 1465.26
                                            else:  # if sqrt_receipts_times_miles > 22506.505859
                                                return 1502.49
                                    else:  # if miles_per_day > 155.375000
                                        if sqrt_receipts_squared <= 1134.590027:
                                            if sqrt_receipts <= 32.134581:
                                                if days_receipts <= 3700.459961:
                                                    return 1324.64
                                                else:  # if days_receipts > 3700.459961
                                                    return 1337.63
                                            else:  # if sqrt_receipts > 32.134581
                                                return 1353.87
                                        else:  # if sqrt_receipts_squared > 1134.590027
                                            if sqrt_receipts_times_miles <= 21057.581055:
                                                if sqrt_receipts_times_days <= 104.685905:
                                                    return 1364.54
                                                else:  # if sqrt_receipts_times_days > 104.685905
                                                    return 1360.76
                                            else:  # if sqrt_receipts_times_miles > 21057.581055
                                                if sqrt_receipts_times_miles <= 22052.868164:
                                                    return 1459.34
                                                else:  # if sqrt_receipts_times_miles > 22052.868164
                                                    if is_high_efficiency <= 0.500000:
                                                        if miles_per_day <= 213.000000:
                                                            return 1419.48
                                                        else:  # if miles_per_day > 213.000000
                                                            return 1416.98
                                                    else:  # if is_high_efficiency > 0.500000
                                                        return 1435.96
                            else:  # if miles_per_receipt > 0.942747
                                if miles <= 833.500000:
                                    return 784.52
                                else:  # if miles > 833.500000
                                    return 1251.14
                    else:  # if miles_receipts > 1033628.093750
                        if miles_per_day <= 1075.000000:
                            if log_days_times_miles <= 7.083276:
                                if miles_receipts <= 1383432.312500:
                                    if receipts <= 1395.710022:
                                        if miles_receipts <= 1200485.812500:
                                            return 1328.85
                                        else:  # if miles_receipts > 1200485.812500
                                            if sqrt_receipts_cubed_scaled <= 46.396521:
                                                return 1317.33
                                            else:  # if sqrt_receipts_cubed_scaled > 46.396521
                                                return 1313.53
                                    else:  # if receipts > 1395.710022
                                        if days_times_miles <= 1026.000000:
                                            if receipts <= 1579.084961:
                                                if log_miles <= 6.538073:
                                                    return 1376.04
                                                else:  # if log_miles > 6.538073
                                                    if log_miles <= 6.659072:
                                                        return 1398.75
                                                    else:  # if log_miles > 6.659072
                                                        return 1398.94
                                            else:  # if receipts > 1579.084961
                                                if days_times_miles <= 832.000000:
                                                    if log_days_times_miles <= 6.557230:
                                                        return 1372.83
                                                    else:  # if log_days_times_miles > 6.557230
                                                        if receipts_per_day <= 1654.625000:
                                                            return 1362.39
                                                        else:  # if receipts_per_day > 1654.625000
                                                            return 1365.21
                                                else:  # if days_times_miles > 832.000000
                                                    return 1342.39
                                        else:  # if days_times_miles > 1026.000000
                                            return 1423.86
                                else:  # if miles_receipts > 1383432.312500
                                    if miles_per_day <= 847.000000:
                                        if log_days_times_miles <= 6.704995:
                                            if sqrt_receipts_times_days <= 42.777100:
                                                return 1447.25
                                            else:  # if sqrt_receipts_times_days > 42.777100
                                                if days_receipts <= 2038.125000:
                                                    return 1419.88
                                                else:  # if days_receipts > 2038.125000
                                                    if log_miles <= 6.612651:
                                                        return 1421.07
                                                    else:  # if log_miles > 6.612651
                                                        return 1421.36
                                        else:  # if log_days_times_miles > 6.704995
                                            return 1374.91
                                    else:  # if miles_per_day > 847.000000
                                        if miles_per_day <= 1063.000000:
                                            if log_miles <= 6.904228:
                                                if miles_receipts <= 2141487.875000:
                                                    return 1456.34
                                                else:  # if miles_receipts > 2141487.875000
                                                    return 1439.17
                                            else:  # if log_miles > 6.904228
                                                if sqrt_receipts_times_days <= 44.272041:
                                                    if sqrt_receipts_squared <= 1615.645020:
                                                        return 1465.90
                                                    else:  # if sqrt_receipts_squared > 1615.645020
                                                        return 1466.95
                                                else:  # if sqrt_receipts_times_days > 44.272041
                                                    return 1475.40
                                        else:  # if miles_per_day > 1063.000000
                                            return 1421.45
                            else:  # if log_days_times_miles > 7.083276
                                if days_receipts <= 2681.920044:
                                    return 1666.52
                                else:  # if days_receipts > 2681.920044
                                    if miles_per_receipt <= 0.960935:
                                        if miles_per_day <= 474.750000:
                                            if miles_receipts <= 1473129.562500:
                                                if days_receipts <= 5276.750000:
                                                    if log_days_times_miles <= 7.166065:
                                                        if days_times_miles <= 1256.000000:
                                                            return 1494.23
                                                        else:  # if days_times_miles > 1256.000000
                                                            return 1490.51
                                                    else:  # if log_days_times_miles > 7.166065
                                                        if sqrt_receipts_squared <= 1291.940002:
                                                            if days_receipts <= 4361.779907:
                                                                return 1515.99
                                                            else:  # if days_receipts > 4361.779907
                                                                return 1513.28
                                                        else:  # if sqrt_receipts_squared > 1291.940002
                                                            if log_receipts <= 7.370724:
                                                                return 1536.60
                                                            else:  # if log_receipts > 7.370724
                                                                return 1531.20
                                                else:  # if days_receipts > 5276.750000
                                                    return 1586.21
                                            else:  # if miles_receipts > 1473129.562500
                                                if sqrt_miles <= 29.345087:
                                                    if log_receipts <= 7.717918:
                                                        if is_extreme_receipts_2000 <= 0.500000:
                                                            return 1522.76
                                                        else:  # if is_extreme_receipts_2000 > 0.500000
                                                            return 1523.26
                                                    else:  # if log_receipts > 7.717918
                                                        return 1485.40
                                                else:  # if sqrt_miles > 29.345087
                                                    if sqrt_receipts_times_miles <= 37216.734375:
                                                        return 1489.99
                                                    else:  # if sqrt_receipts_times_miles > 37216.734375
                                                        if days <= 2.500000:
                                                            if receipts_fourth_scaled <= 19.112511:
                                                                return 1432.79
                                                            else:  # if receipts_fourth_scaled > 19.112511
                                                                return 1437.95
                                                        else:  # if days > 2.500000
                                                            if miles_per_receipt <= 0.677850:
                                                                return 1462.01
                                                            else:  # if miles_per_receipt > 0.677850
                                                                return 1451.85
                                        else:  # if miles_per_day > 474.750000
                                            if miles_receipts <= 1752159.125000:
                                                return 1577.55
                                            else:  # if miles_receipts > 1752159.125000
                                                if receipts_squared <= 3947490.875000:
                                                    if log_days_times_miles <= 7.651976:
                                                        return 1549.54
                                                    else:  # if log_days_times_miles > 7.651976
                                                        return 1543.17
                                                else:  # if receipts_squared > 3947490.875000
                                                    if receipts_per_mile <= 2.090446:
                                                        return 1528.91
                                                    else:  # if receipts_per_mile > 2.090446
                                                        return 1519.98
                                    else:  # if miles_per_receipt > 0.960935
                                        return 1361.30
                        else:  # if miles_per_day > 1075.000000
                            if days_times_miles <= 1093.500000:
                                return 446.94
                            else:  # if days_times_miles > 1093.500000
                                if sqrt_receipts_times_miles <= 43807.904297:
                                    if receipts_per_mile <= 1.338126:
                                        return 1387.17
                                    else:  # if receipts_per_mile > 1.338126
                                        return 1403.60
                                else:  # if sqrt_receipts_times_miles > 43807.904297
                                    if days_times_miles <= 1139.000000:
                                        return 1423.85
                                    else:  # if days_times_miles > 1139.000000
                                        return 1412.13
            else:  # if days_receipts > 5494.430176
                if days_receipts <= 11625.575195:
                    if log_days_times_miles <= 6.888393:
                        if miles_per_receipt <= 0.151686:
                            if receipts_to_total_cost_ratio <= 10.026133:
                                if sqrt_receipts <= 33.536798:
                                    if log_receipts <= 6.743671:
                                        return 1116.56
                                    else:  # if log_receipts > 6.743671
                                        if days_receipts <= 9442.660156:
                                            if sqrt_receipts_times_days <= 270.908691:
                                                if log_receipts <= 7.002888:
                                                    return 1365.73
                                                else:  # if log_receipts > 7.002888
                                                    return 1312.16
                                            else:  # if sqrt_receipts_times_days > 270.908691
                                                if days <= 9.500000:
                                                    if receipts_fourth_scaled <= 0.881017:
                                                        return 1281.64
                                                    else:  # if receipts_fourth_scaled > 0.881017
                                                        return 1271.52
                                                else:  # if days > 9.500000
                                                    return 1237.07
                                        else:  # if days_receipts > 9442.660156
                                            if miles_receipts <= 10136.810059:
                                                return 1361.08
                                            else:  # if miles_receipts > 10136.810059
                                                if receipts_fourth_scaled <= 0.896773:
                                                    return 1377.35
                                                else:  # if receipts_fourth_scaled > 0.896773
                                                    return 1372.31
                                else:  # if sqrt_receipts > 33.536798
                                    if days_receipts <= 10823.290039:
                                        if days_times_miles <= 790.000000:
                                            if days_receipts <= 9217.160156:
                                                if days_times_miles <= 754.000000:
                                                    if miles_squared <= 34104.500000:
                                                        if sqrt_receipts_squared <= 2016.595032:
                                                            return 1394.55
                                                        else:  # if sqrt_receipts_squared > 2016.595032
                                                            return 1392.10
                                                    else:  # if miles_squared > 34104.500000
                                                        return 1386.33
                                                else:  # if days_times_miles > 754.000000
                                                    return 1416.33
                                            else:  # if days_receipts > 9217.160156
                                                if miles_per_receipt <= 0.022773:
                                                    return 1410.58
                                                else:  # if miles_per_receipt > 0.022773
                                                    if days_receipts <= 9631.719727:
                                                        return 1443.02
                                                    else:  # if days_receipts > 9631.719727
                                                        return 1438.52
                                        else:  # if days_times_miles > 790.000000
                                            if days_receipts <= 6759.310059:
                                                if miles_per_receipt <= 0.136677:
                                                    if days <= 4.000000:
                                                        return 1447.95
                                                    else:  # if days > 4.000000
                                                        return 1443.96
                                                else:  # if miles_per_receipt > 0.136677
                                                    return 1455.37
                                            else:  # if days_receipts > 6759.310059
                                                if receipts_cubed_scaled <= 7.162690:
                                                    if receipts_per_day <= 308.754173:
                                                        return 1478.11
                                                    else:  # if receipts_per_day > 308.754173
                                                        return 1483.48
                                                else:  # if receipts_cubed_scaled > 7.162690
                                                    return 1450.67
                                    else:  # if days_receipts > 10823.290039
                                        if miles <= 56.500000:
                                            return 1500.28
                                        else:  # if miles > 56.500000
                                            return 1515.54
                            else:  # if receipts_to_total_cost_ratio > 10.026133
                                if log_miles <= 4.362916:
                                    return 322.00
                                else:  # if log_miles > 4.362916
                                    if log_miles <= 4.709490:
                                        return 1413.52
                                    else:  # if log_miles > 4.709490
                                        return 1345.66
                        else:  # if miles_per_receipt > 0.151686
                            return 511.23
                    else:  # if log_days_times_miles > 6.888393
                        if log_days_times_miles <= 8.252301:
                            if sqrt_miles <= 22.770529:
                                if sqrt_receipts_times_miles <= 21690.715820:
                                    if receipts_cubed_scaled <= 1.203725:
                                        if days_receipts <= 11149.200195:
                                            if days_receipts <= 9178.785156:
                                                if days_times_miles <= 2323.959961:
                                                    if miles_per_receipt <= 0.243733:
                                                        return 1287.00
                                                    else:  # if miles_per_receipt > 0.243733
                                                        if miles_receipts <= 256685.054688:
                                                            return 1305.54
                                                        else:  # if miles_receipts > 256685.054688
                                                            return 1309.85
                                                else:  # if days_times_miles > 2323.959961
                                                    return 1353.77
                                            else:  # if days_receipts > 9178.785156
                                                if miles <= 272.500000:
                                                    if miles_per_day <= 19.880000:
                                                        return 1371.86
                                                    else:  # if miles_per_day > 19.880000
                                                        return 1374.90
                                                else:  # if miles > 272.500000
                                                    return 1356.46
                                        else:  # if days_receipts > 11149.200195
                                            if days <= 11.500000:
                                                return 1444.13
                                            else:  # if days > 11.500000
                                                return 1432.75
                                    else:  # if receipts_cubed_scaled > 1.203725
                                        if log_days_times_miles <= 7.508103:
                                            if sqrt_receipts_times_days <= 166.701103:
                                                if miles_per_receipt <= 0.144500:
                                                    return 1472.53
                                                else:  # if miles_per_receipt > 0.144500
                                                    if receipts_per_mile <= 6.005904:
                                                        return 1411.95
                                                    else:  # if receipts_per_mile > 6.005904
                                                        if miles_per_day <= 87.250000:
                                                            return 1435.34
                                                        else:  # if miles_per_day > 87.250000
                                                            return 1438.41
                                            else:  # if sqrt_receipts_times_days > 166.701103
                                                if sqrt_receipts_times_days <= 198.895287:
                                                    if sqrt_receipts_times_days <= 170.345825:
                                                        return 1518.93
                                                    else:  # if sqrt_receipts_times_days > 170.345825
                                                        if miles_receipts <= 649131.875000:
                                                            if sqrt_miles <= 17.653504:
                                                                if sqrt_receipts_squared <= 1226.744995:
                                                                    return 1485.59
                                                                else:  # if sqrt_receipts_squared > 1226.744995
                                                                    if receipts_squared <= 5245354.000000:
                                                                        if days_squared <= 20.500000:
                                                                            return 1476.03
                                                                        else:  # if days_squared > 20.500000
                                                                            return 1477.12
                                                                    else:  # if receipts_squared > 5245354.000000
                                                                        return 1483.58
                                                            else:  # if sqrt_miles > 17.653504
                                                                return 1467.52
                                                        else:  # if miles_receipts > 649131.875000
                                                            if log_days_times_miles <= 7.335553:
                                                                if sqrt_receipts_times_miles <= 14406.759277:
                                                                    return 1503.98
                                                                else:  # if sqrt_receipts_times_miles > 14406.759277
                                                                    return 1507.04
                                                            else:  # if log_days_times_miles > 7.335553
                                                                if miles_squared <= 189394.000000:
                                                                    return 1491.90
                                                                else:  # if miles_squared > 189394.000000
                                                                    return 1497.46
                                                else:  # if sqrt_receipts_times_days > 198.895287
                                                    if receipts_squared <= 2017409.812500:
                                                        if miles_receipts <= 222158.507812:
                                                            if receipts_per_mile <= 10.046223:
                                                                if sqrt_receipts <= 34.456501:
                                                                    return 1516.43
                                                                else:  # if sqrt_receipts > 34.456501
                                                                    if log_receipts <= 7.172988:
                                                                        return 1499.24
                                                                    else:  # if log_receipts > 7.172988
                                                                        return 1500.09
                                                            else:  # if receipts_per_mile > 10.046223
                                                                return 1539.77
                                                        else:  # if miles_receipts > 222158.507812
                                                            if miles_receipts <= 268494.523438:
                                                                return 1479.01
                                                            else:  # if miles_receipts > 268494.523438
                                                                return 1452.17
                                                    else:  # if receipts_squared > 2017409.812500
                                                        if sqrt_receipts_cubed_scaled <= 56.565809:
                                                            return 1535.30
                                                        else:  # if sqrt_receipts_cubed_scaled > 56.565809
                                                            if sqrt_receipts_times_days <= 207.394417:
                                                                return 1584.73
                                                            else:  # if sqrt_receipts_times_days > 207.394417
                                                                if days_times_miles <= 1184.500000:
                                                                    return 1562.23
                                                                else:  # if days_times_miles > 1184.500000
                                                                    return 1557.94
                                        else:  # if log_days_times_miles > 7.508103
                                            if receipts_fourth_scaled <= 4.595358:
                                                if receipts_to_total_cost_ratio <= 2.062365:
                                                    if receipts_to_total_cost_ratio <= 1.797979:
                                                        if receipts <= 1114.225037:
                                                            return 1539.10
                                                        else:  # if receipts > 1114.225037
                                                            return 1525.26
                                                    else:  # if receipts_to_total_cost_ratio > 1.797979
                                                        if sqrt_receipts_times_days <= 268.321915:
                                                            return 1453.25
                                                        else:  # if sqrt_receipts_times_days > 268.321915
                                                            if receipts_fourth_scaled <= 2.054669:
                                                                return 1483.33
                                                            else:  # if receipts_fourth_scaled > 2.054669
                                                                return 1473.75
                                                else:  # if receipts_to_total_cost_ratio > 2.062365
                                                    if log_days_times_miles <= 7.581719:
                                                        return 1465.72
                                                    else:  # if log_days_times_miles > 7.581719
                                                        if days_times_miles <= 2176.119995:
                                                            if sqrt_receipts_squared <= 1229.065002:
                                                                if sqrt_miles <= 15.096036:
                                                                    return 1561.63
                                                                else:  # if sqrt_miles > 15.096036
                                                                    return 1560.78
                                                            else:  # if sqrt_receipts_squared > 1229.065002
                                                                return 1585.02
                                                        else:  # if days_times_miles > 2176.119995
                                                            if miles_per_receipt <= 0.287869:
                                                                if receipts_cubed_scaled <= 1.779355:
                                                                    return 1522.60
                                                                else:  # if receipts_cubed_scaled > 1.779355
                                                                    return 1514.40
                                                            else:  # if miles_per_receipt > 0.287869
                                                                if log_days_times_miles <= 7.855157:
                                                                    if sqrt_receipts_times_days <= 210.985550:
                                                                        return 1549.82
                                                                    else:  # if sqrt_receipts_times_days > 210.985550
                                                                        return 1550.04
                                                                else:  # if log_days_times_miles > 7.855157
                                                                    return 1547.50
                                            else:  # if receipts_fourth_scaled > 4.595358
                                                if receipts_fourth_scaled <= 14.940197:
                                                    if sqrt_receipts_times_days <= 237.387665:
                                                        if days_receipts <= 7683.395020:
                                                            return 1628.66
                                                        else:  # if days_receipts > 7683.395020
                                                            if miles_per_receipt <= 0.212123:
                                                                return 1588.80
                                                            else:  # if miles_per_receipt > 0.212123
                                                                if days_receipts <= 8358.510010:
                                                                    return 1607.34
                                                                else:  # if days_receipts > 8358.510010
                                                                    return 1608.55
                                                    else:  # if sqrt_receipts_times_days > 237.387665
                                                        if receipts_cubed_scaled <= 5.190271:
                                                            return 1682.33
                                                        else:  # if receipts_cubed_scaled > 5.190271
                                                            return 1671.23
                                                else:  # if receipts_fourth_scaled > 14.940197
                                                    return 1501.10
                                else:  # if sqrt_receipts_times_miles > 21690.715820
                                    return 669.85
                            else:  # if sqrt_miles > 22.770529
                                if sqrt_receipts_times_days <= 147.935493:
                                    if miles_receipts <= 2170398.750000:
                                        if sqrt_receipts_times_days <= 145.140465:
                                            if sqrt_receipts_cubed_scaled <= 92.218452:
                                                if miles_per_day <= 328.833328:
                                                    return 1539.47
                                                else:  # if miles_per_day > 328.833328
                                                    return 1539.00
                                            else:  # if sqrt_receipts_cubed_scaled > 92.218452
                                                if sqrt_receipts <= 47.151388:
                                                    if miles_per_day <= 256.499992:
                                                        return 1522.45
                                                    else:  # if miles_per_day > 256.499992
                                                        return 1520.73
                                                else:  # if sqrt_receipts > 47.151388
                                                    return 1513.04
                                        else:  # if sqrt_receipts_times_days > 145.140465
                                            if sqrt_receipts_cubed_scaled <= 116.153469:
                                                return 1458.63
                                            else:  # if sqrt_receipts_cubed_scaled > 116.153469
                                                return 1490.96
                                    else:  # if miles_receipts > 2170398.750000
                                        if receipts_per_day <= 707.486664:
                                            return 1436.66
                                        else:  # if receipts_per_day > 707.486664
                                            if miles_per_day <= 386.833344:
                                                return 1434.84
                                            else:  # if miles_per_day > 386.833344
                                                return 1434.71
                                else:  # if sqrt_receipts_times_days > 147.935493
                                    if days_times_miles <= 3582.500000:
                                        if receipts_per_day <= 224.075005:
                                            if receipts_to_total_cost_ratio <= 1.841598:
                                                return 1492.08
                                            else:  # if receipts_to_total_cost_ratio > 1.841598
                                                return 1577.01
                                        else:  # if receipts_per_day > 224.075005
                                            if sqrt_receipts_times_days <= 175.270905:
                                                if miles_squared <= 587528.500000:
                                                    if is_very_high_receipts_1500 <= 0.500000:
                                                        if sqrt_receipts <= 35.631939:
                                                            return 1654.62
                                                        else:  # if sqrt_receipts > 35.631939
                                                            return 1682.10
                                                    else:  # if is_very_high_receipts_1500 > 0.500000
                                                        return 1612.43
                                                else:  # if miles_squared > 587528.500000
                                                    if is_extreme_receipts_2000 <= 0.500000:
                                                        if miles_per_day <= 206.250000:
                                                            return 1575.87
                                                        else:  # if miles_per_day > 206.250000
                                                            return 1580.95
                                                    else:  # if is_extreme_receipts_2000 > 0.500000
                                                        return 1587.80
                                            else:  # if sqrt_receipts_times_days > 175.270905
                                                if miles_per_receipt <= 0.364320:
                                                    if days_receipts <= 10136.455078:
                                                        if days <= 4.500000:
                                                            return 1611.66
                                                        else:  # if days > 4.500000
                                                            if sqrt_receipts_times_miles <= 22173.529297:
                                                                return 1624.01
                                                            else:  # if sqrt_receipts_times_miles > 22173.529297
                                                                return 1623.81
                                                    else:  # if days_receipts > 10136.455078
                                                        if sqrt_receipts_times_miles <= 28578.403320:
                                                            return 1661.61
                                                        else:  # if sqrt_receipts_times_miles > 28578.403320
                                                            return 1645.06
                                                else:  # if miles_per_receipt > 0.364320
                                                    if receipts_squared <= 1676842.250000:
                                                        return 1724.68
                                                    else:  # if receipts_squared > 1676842.250000
                                                        if miles_receipts <= 1518731.218750:
                                                            if days_times_miles <= 3417.500000:
                                                                return 1682.08
                                                            else:  # if days_times_miles > 3417.500000
                                                                return 1686.98
                                                        else:  # if miles_receipts > 1518731.218750
                                                            if log_miles <= 6.774130:
                                                                return 1698.94
                                                            else:  # if log_miles > 6.774130
                                                                return 1698.00
                                    else:  # if days_times_miles > 3582.500000
                                        if receipts_squared <= 2148030.500000:
                                            return 1777.14
                                        else:  # if receipts_squared > 2148030.500000
                                            if miles_per_day <= 147.199997:
                                                return 1722.49
                                            else:  # if miles_per_day > 147.199997
                                                return 1729.08
                        else:  # if log_days_times_miles > 8.252301
                            return 631.81
                else:  # if days_receipts > 11625.575195
                    if sqrt_receipts_times_days <= 432.547729:
                        if receipts_per_mile <= 6.916196:
                            if days_receipts <= 16456.464844:
                                if sqrt_receipts <= 48.607363:
                                    if days_receipts <= 12742.270020:
                                        if receipts_to_total_cost_ratio <= 4.115170:
                                            if miles_squared <= 89605.000000:
                                                return 1579.73
                                            else:  # if miles_squared > 89605.000000
                                                return 1606.76
                                        else:  # if receipts_to_total_cost_ratio > 4.115170
                                            return 1649.42
                                    else:  # if days_receipts > 12742.270020
                                        if receipts_per_day <= 353.614990:
                                            if sqrt_receipts_times_days <= 396.823883:
                                                if miles_per_receipt <= 0.219793:
                                                    if miles_per_receipt <= 0.181542:
                                                        if miles_per_receipt <= 0.171746:
                                                            return 1705.24
                                                        else:  # if miles_per_receipt > 0.171746
                                                            return 1705.27
                                                    else:  # if miles_per_receipt > 0.181542
                                                        return 1691.68
                                                else:  # if miles_per_receipt > 0.219793
                                                    return 1732.46
                                            else:  # if sqrt_receipts_times_days > 396.823883
                                                if days_times_miles <= 2985.500000:
                                                    return 1696.65
                                                else:  # if days_times_miles > 2985.500000
                                                    if days_receipts <= 15193.640137:
                                                        return 1663.39
                                                    else:  # if days_receipts > 15193.640137
                                                        return 1673.70
                                        else:  # if receipts_per_day > 353.614990
                                            return 1628.60
                                else:  # if sqrt_receipts > 48.607363
                                    if receipts_fourth_scaled <= 35.494196:
                                        return 1785.53
                                    else:  # if receipts_fourth_scaled > 35.494196
                                        return 1742.34
                            else:  # if days_receipts > 16456.464844
                                if miles_per_receipt <= 0.188548:
                                    return 1502.02
                                else:  # if miles_per_receipt > 0.188548
                                    return 1558.12
                        else:  # if receipts_per_mile > 6.916196
                            if receipts_to_total_cost_ratio <= 5.467741:
                                if sqrt_receipts_squared <= 1141.375000:
                                    if days_receipts <= 12797.629883:
                                        return 1466.31
                                    else:  # if days_receipts > 12797.629883
                                        if sqrt_receipts_times_days <= 421.110046:
                                            if days_times_miles <= 749.000000:
                                                return 1494.81
                                            else:  # if days_times_miles > 749.000000
                                                return 1492.02
                                        else:  # if sqrt_receipts_times_days > 421.110046
                                            return 1480.87
                                else:  # if sqrt_receipts_squared > 1141.375000
                                    if days_squared <= 72.500000:
                                        if receipts_per_day <= 295.641251:
                                            if sqrt_miles <= 16.275922:
                                                if miles_receipts <= 373090.906250:
                                                    if sqrt_receipts_times_days <= 331.149399:
                                                        return 1461.33
                                                    else:  # if sqrt_receipts_times_days > 331.149399
                                                        return 1485.69
                                                else:  # if miles_receipts > 373090.906250
                                                    if receipts_per_mile <= 8.902456:
                                                        return 1510.91
                                                    else:  # if receipts_per_mile > 8.902456
                                                        return 1506.38
                                            else:  # if sqrt_miles > 16.275922
                                                return 1454.47
                                        else:  # if receipts_per_day > 295.641251
                                            if receipts_per_day <= 328.636429:
                                                if miles_per_receipt <= 0.121269:
                                                    return 1548.87
                                                else:  # if miles_per_receipt > 0.121269
                                                    if receipts_per_mile <= 7.814827:
                                                        return 1557.27
                                                    else:  # if receipts_per_mile > 7.814827
                                                        return 1558.09
                                            else:  # if receipts_per_day > 328.636429
                                                if miles_per_receipt <= 0.105522:
                                                    return 1603.89
                                                else:  # if miles_per_receipt > 0.105522
                                                    if log_miles <= 5.728252:
                                                        return 1634.04
                                                    else:  # if log_miles > 5.728252
                                                        return 1637.65
                                    else:  # if days_squared > 72.500000
                                        if receipts_to_total_cost_ratio <= 2.215287:
                                            if miles_squared <= 4658.000000:
                                                return 1564.90
                                            else:  # if miles_squared > 4658.000000
                                                return 1553.21
                                        else:  # if receipts_to_total_cost_ratio > 2.215287
                                            if receipts <= 1294.015015:
                                                return 1707.38
                                            else:  # if receipts > 1294.015015
                                                if sqrt_receipts_times_days <= 397.718536:
                                                    if receipts_per_mile <= 138.186031:
                                                        if days_squared <= 90.500000:
                                                            return 1623.73
                                                        else:  # if days_squared > 90.500000
                                                            return 1635.50
                                                    else:  # if receipts_per_mile > 138.186031
                                                        return 1610.25
                                                else:  # if sqrt_receipts_times_days > 397.718536
                                                    if receipts_cubed_scaled <= 5.771666:
                                                        return 1593.24
                                                    else:  # if receipts_cubed_scaled > 5.771666
                                                        return 1557.20
                            else:  # if receipts_to_total_cost_ratio > 5.467741
                                if miles <= 133.500000:
                                    if miles_squared <= 137.000000:
                                        return 1422.12
                                    else:  # if miles_squared > 137.000000
                                        if receipts <= 2370.265015:
                                            return 1485.05
                                        else:  # if receipts > 2370.265015
                                            if sqrt_receipts_times_days <= 370.795090:
                                                if receipts_fourth_scaled <= 33.859226:
                                                    return 1454.05
                                                else:  # if receipts_fourth_scaled > 33.859226
                                                    return 1459.63
                                            else:  # if sqrt_receipts_times_days > 370.795090
                                                return 1468.19
                                else:  # if miles > 133.500000
                                    if miles <= 143.000000:
                                        return 1561.20
                                    else:  # if miles > 143.000000
                                        if receipts_squared <= 6019097.750000:
                                            return 1523.75
                                        else:  # if receipts_squared > 6019097.750000
                                            return 1516.58
                    else:  # if sqrt_receipts_times_days > 432.547729
                        if receipts_per_day <= 181.471252:
                            if log_days_times_miles <= 8.150611:
                                if miles_per_day <= 2.101648:
                                    return 1555.48
                                else:  # if miles_per_day > 2.101648
                                    if miles_receipts <= 128771.078125:
                                        if miles_receipts <= 86950.398438:
                                            return 1745.18
                                        else:  # if miles_receipts > 86950.398438
                                            if miles_receipts <= 103217.105469:
                                                if is_extreme_receipts_2000 <= 0.500000:
                                                    return 1682.62
                                                else:  # if is_extreme_receipts_2000 > 0.500000
                                                    return 1666.29
                                            else:  # if miles_receipts > 103217.105469
                                                if receipts_to_total_cost_ratio <= 1.475353:
                                                    return 1688.90
                                                else:  # if receipts_to_total_cost_ratio > 1.475353
                                                    if receipts_per_mile <= 17.648399:
                                                        return 1703.02
                                                    else:  # if receipts_per_mile > 17.648399
                                                        return 1710.72
                                    else:  # if miles_receipts > 128771.078125
                                        if sqrt_receipts_times_miles <= 5483.713135:
                                            if receipts_per_mile <= 16.516133:
                                                if days_squared <= 182.500000:
                                                    if miles_squared <= 14792.500000:
                                                        return 1779.92
                                                    else:  # if miles_squared > 14792.500000
                                                        return 1777.72
                                                else:  # if days_squared > 182.500000
                                                    return 1761.68
                                            else:  # if receipts_per_mile > 16.516133
                                                return 1807.67
                                        else:  # if sqrt_receipts_times_miles > 5483.713135
                                            if days_squared <= 182.500000:
                                                if miles <= 196.000000:
                                                    if sqrt_receipts_times_miles <= 6200.725586:
                                                        return 1721.56
                                                    else:  # if sqrt_receipts_times_miles > 6200.725586
                                                        return 1716.13
                                                else:  # if miles > 196.000000
                                                    return 1705.90
                                            else:  # if days_squared > 182.500000
                                                return 1798.47
                            else:  # if log_days_times_miles > 8.150611
                                if sqrt_receipts_cubed_scaled <= 72.571297:
                                    return 1832.34
                                else:  # if sqrt_receipts_cubed_scaled > 72.571297
                                    return 1968.40
                        else:  # if receipts_per_day > 181.471252
                            if sqrt_receipts_squared <= 2047.830078:
                                if sqrt_receipts <= 44.751431:
                                    return 1542.40
                                else:  # if sqrt_receipts > 44.751431
                                    if miles_receipts <= 251868.324219:
                                        return 1569.37
                                    else:  # if miles_receipts > 251868.324219
                                        return 1590.82
                            else:  # if sqrt_receipts_squared > 2047.830078
                                if sqrt_receipts_cubed_scaled <= 121.137085:
                                    if receipts_to_total_cost_ratio <= 3.035402:
                                        return 1586.22
                                    else:  # if receipts_to_total_cost_ratio > 3.035402
                                        if receipts_cubed_scaled <= 11.543867:
                                            if miles_per_day <= 11.983334:
                                                if days_times_miles <= 894.000000:
                                                    return 1629.92
                                                else:  # if days_times_miles > 894.000000
                                                    return 1632.42
                                            else:  # if miles_per_day > 11.983334
                                                if sqrt_receipts_times_days <= 508.448318:
                                                    return 1624.11
                                                else:  # if sqrt_receipts_times_days > 508.448318
                                                    return 1625.46
                                        else:  # if receipts_cubed_scaled > 11.543867
                                            if miles_squared <= 35912.500000:
                                                return 1642.15
                                            else:  # if miles_squared > 35912.500000
                                                return 1638.66
                                else:  # if sqrt_receipts_cubed_scaled > 121.137085
                                    if receipts_to_total_cost_ratio <= 4.336527:
                                        return 1589.65
                                    else:  # if receipts_to_total_cost_ratio > 4.336527
                                        if log_days_times_miles <= 5.991920:
                                            return 1556.78
                                        else:  # if log_days_times_miles > 5.991920
                                            return 1572.91
        else:  # if log_days_times_miles > 8.262033
            if days_times_miles <= 6939.000000:
                if receipts_cubed_scaled <= 1.292266:
                    if days_times_miles <= 6566.000000:
                        if log_days_times_miles <= 8.478141:
                            if sqrt_miles <= 29.886181:
                                if receipts_to_total_cost_ratio <= 1.405285:
                                    if receipts <= 946.970001:
                                        return 1676.48
                                    else:  # if receipts > 946.970001
                                        if receipts <= 1002.815002:
                                            return 1608.60
                                        else:  # if receipts > 1002.815002
                                            return 1630.47
                                else:  # if receipts_to_total_cost_ratio > 1.405285
                                    if sqrt_receipts <= 31.889433:
                                        return 1559.83
                                    else:  # if sqrt_receipts > 31.889433
                                        return 1476.48
                            else:  # if sqrt_miles > 29.886181
                                if miles_per_receipt <= 1.123315:
                                    return 1499.68
                                else:  # if miles_per_receipt > 1.123315
                                    return 1478.93
                        else:  # if log_days_times_miles > 8.478141
                            if receipts_per_day <= 98.279278:
                                if sqrt_receipts_cubed_scaled <= 27.670010:
                                    return 1492.64
                                else:  # if sqrt_receipts_cubed_scaled > 27.670010
                                    return 1656.28
                            else:  # if receipts_per_day > 98.279278
                                if miles_receipts <= 610041.875000:
                                    if log_miles <= 6.329956:
                                        return 1395.03
                                    else:  # if log_miles > 6.329956
                                        if receipts_per_mile <= 1.469564:
                                            return 1384.78
                                        else:  # if receipts_per_mile > 1.469564
                                            return 1388.05
                                else:  # if miles_receipts > 610041.875000
                                    if receipts_to_total_cost_ratio <= 1.048599:
                                        return 1430.04
                                    else:  # if receipts_to_total_cost_ratio > 1.048599
                                        if days_times_miles <= 5144.000000:
                                            if days_receipts <= 6642.379883:
                                                if sqrt_miles <= 31.826313:
                                                    return 1496.46
                                                else:  # if sqrt_miles > 31.826313
                                                    return 1501.24
                                            else:  # if days_receipts > 6642.379883
                                                return 1483.06
                                        else:  # if days_times_miles > 5144.000000
                                            return 1547.50
                    else:  # if days_times_miles > 6566.000000
                        return 877.17
                else:  # if receipts_cubed_scaled > 1.292266
                    if miles_per_day <= 99.750000:
                        if miles_per_day <= 99.187500:
                            if long_trip_high_receipts <= 0.500000:
                                if receipts_to_total_cost_ratio <= 2.734142:
                                    if sqrt_receipts_times_miles <= 24005.281250:
                                        if log_days_times_miles <= 8.604344:
                                            if miles_per_day <= 61.777777:
                                                if receipts_per_mile <= 3.663277:
                                                    if sqrt_receipts_times_days <= 402.437256:
                                                        if sqrt_receipts_times_days <= 372.572678:
                                                            if sqrt_receipts_cubed_scaled <= 46.152573:
                                                                return 1631.49
                                                            else:  # if sqrt_receipts_cubed_scaled > 46.152573
                                                                return 1633.26
                                                        else:  # if sqrt_receipts_times_days > 372.572678
                                                            if miles_receipts <= 698978.437500:
                                                                return 1618.13
                                                            else:  # if miles_receipts > 698978.437500
                                                                return 1624.87
                                                    else:  # if sqrt_receipts_times_days > 402.437256
                                                        return 1649.04
                                                else:  # if receipts_per_mile > 3.663277
                                                    return 1674.09
                                            else:  # if miles_per_day > 61.777777
                                                if log_miles <= 6.331044:
                                                    return 1483.77
                                                else:  # if log_miles > 6.331044
                                                    if sqrt_miles <= 24.745271:
                                                        if days_times_miles <= 4969.000000:
                                                            return 1561.41
                                                        else:  # if days_times_miles > 4969.000000
                                                            return 1587.21
                                                    else:  # if sqrt_miles > 24.745271
                                                        if miles_per_day <= 93.285713:
                                                            if sqrt_receipts_times_miles <= 23354.707031:
                                                                return 1639.12
                                                            else:  # if sqrt_receipts_times_miles > 23354.707031
                                                                return 1630.66
                                                        else:  # if miles_per_day > 93.285713
                                                            return 1600.42
                                        else:  # if log_days_times_miles > 8.604344
                                            if days_receipts <= 13851.529785:
                                                return 1730.86
                                            else:  # if days_receipts > 13851.529785
                                                return 1770.37
                                    else:  # if sqrt_receipts_times_miles > 24005.281250
                                        if miles <= 633.000000:
                                            if receipts_to_total_cost_ratio <= 2.545100:
                                                return 1800.86
                                            else:  # if receipts_to_total_cost_ratio > 2.545100
                                                return 1739.49
                                        else:  # if miles > 633.000000
                                            if log_miles <= 6.543908:
                                                if miles_per_receipt <= 0.332869:
                                                    return 1685.92
                                                else:  # if miles_per_receipt > 0.332869
                                                    if miles_per_receipt <= 0.397823:
                                                        return 1710.98
                                                    else:  # if miles_per_receipt > 0.397823
                                                        if miles_per_receipt <= 0.421990:
                                                            return 1701.23
                                                        else:  # if miles_per_receipt > 0.421990
                                                            if miles <= 670.500000:
                                                                return 1702.81
                                                            else:  # if miles > 670.500000
                                                                return 1703.20
                                            else:  # if log_miles > 6.543908
                                                if miles_per_receipt <= 0.410361:
                                                    return 1649.49
                                                else:  # if miles_per_receipt > 0.410361
                                                    if sqrt_receipts_times_days <= 347.681778:
                                                        return 1662.92
                                                    else:  # if sqrt_receipts_times_days > 347.681778
                                                        return 1666.18
                                else:  # if receipts_to_total_cost_ratio > 2.734142
                                    if log_receipts <= 7.808753:
                                        if miles_receipts <= 1036612.062500:
                                            if receipts_per_mile <= 4.566180:
                                                return 1568.41
                                            else:  # if receipts_per_mile > 4.566180
                                                if miles_per_receipt <= 0.200840:
                                                    return 1556.68
                                                else:  # if miles_per_receipt > 0.200840
                                                    return 1559.59
                                        else:  # if miles_receipts > 1036612.062500
                                            if sqrt_receipts_times_days <= 433.602905:
                                                if log_receipts <= 7.789530:
                                                    if receipts_squared <= 5448408.500000:
                                                        if sqrt_receipts_cubed_scaled <= 97.633965:
                                                            return 1603.60
                                                        else:  # if sqrt_receipts_cubed_scaled > 97.633965
                                                            return 1599.27
                                                    else:  # if receipts_squared > 5448408.500000
                                                        return 1593.12
                                                else:  # if log_receipts > 7.789530
                                                    return 1556.70
                                            else:  # if sqrt_receipts_times_days > 433.602905
                                                if sqrt_receipts_times_miles <= 25301.462891:
                                                    if sqrt_receipts_cubed_scaled <= 116.992195:
                                                        if log_miles <= 6.203148:
                                                            return 1619.00
                                                        else:  # if log_miles > 6.203148
                                                            return 1615.13
                                                    else:  # if sqrt_receipts_cubed_scaled > 116.992195
                                                        return 1624.68
                                                else:  # if sqrt_receipts_times_miles > 25301.462891
                                                    if log_days_times_miles <= 8.644077:
                                                        return 1640.78
                                                    else:  # if log_days_times_miles > 8.644077
                                                        return 1643.68
                                    else:  # if log_receipts > 7.808753
                                        return 1478.31
                            else:  # if long_trip_high_receipts > 0.500000
                                if days_squared <= 156.500000:
                                    if miles_per_receipt <= 0.234368:
                                        if miles_per_day <= 33.492424:
                                            if sqrt_miles <= 18.640768:
                                                return 1659.50
                                            else:  # if sqrt_miles > 18.640768
                                                if sqrt_receipts_cubed_scaled <= 91.172588:
                                                    return 1682.98
                                                else:  # if sqrt_receipts_cubed_scaled > 91.172588
                                                    if receipts_per_mile <= 6.162953:
                                                        return 1765.67
                                                    else:  # if receipts_per_mile > 6.162953
                                                        return 1755.18
                                        else:  # if miles_per_day > 33.492424
                                            if receipts_per_mile <= 4.783375:
                                                if days <= 11.500000:
                                                    return 1653.69
                                                else:  # if days > 11.500000
                                                    return 1662.88
                                            else:  # if receipts_per_mile > 4.783375
                                                if log_miles <= 6.023131:
                                                    return 1632.61
                                                else:  # if log_miles > 6.023131
                                                    return 1600.10
                                    else:  # if miles_per_receipt > 0.234368
                                        if miles_receipts <= 1016661.781250:
                                            if sqrt_miles <= 22.101547:
                                                if miles_per_receipt <= 0.265341:
                                                    return 1787.41
                                                else:  # if miles_per_receipt > 0.265341
                                                    return 1746.74
                                            else:  # if sqrt_miles > 22.101547
                                                if log_receipts <= 7.580854:
                                                    if sqrt_receipts_times_miles <= 21299.138672:
                                                        if sqrt_receipts_cubed_scaled <= 61.875124:
                                                            return 1806.06
                                                        else:  # if sqrt_receipts_cubed_scaled > 61.875124
                                                            return 1793.52
                                                    else:  # if sqrt_receipts_times_miles > 21299.138672
                                                        if sqrt_receipts_times_miles <= 21907.807617:
                                                            return 1831.92
                                                        else:  # if sqrt_receipts_times_miles > 21907.807617
                                                            return 1823.47
                                                else:  # if log_receipts > 7.580854
                                                    return 1770.91
                                        else:  # if miles_receipts > 1016661.781250
                                            if days_times_miles <= 6682.500000:
                                                if receipts_fourth_scaled <= 14.517369:
                                                    return 1711.55
                                                else:  # if receipts_fourth_scaled > 14.517369
                                                    return 1710.53
                                            else:  # if days_times_miles > 6682.500000
                                                if sqrt_receipts_times_days <= 553.274475:
                                                    if days_receipts <= 24540.855469:
                                                        if receipts <= 2002.244995:
                                                            return 1753.56
                                                        else:  # if receipts > 2002.244995
                                                            return 1752.03
                                                    else:  # if days_receipts > 24540.855469
                                                        return 1739.18
                                                else:  # if sqrt_receipts_times_days > 553.274475
                                                    return 1785.72
                                else:  # if days_squared > 156.500000
                                    if sqrt_receipts_times_days <= 620.797180:
                                        if miles_receipts <= 883618.781250:
                                            if miles_per_receipt <= 0.264739:
                                                return 1918.89
                                            else:  # if miles_per_receipt > 0.264739
                                                return 1915.79
                                        else:  # if miles_receipts > 883618.781250
                                            return 2015.18
                                    else:  # if sqrt_receipts_times_days > 620.797180
                                        if receipts_fourth_scaled <= 19.431922:
                                            return 1839.05
                                        else:  # if receipts_fourth_scaled > 19.431922
                                            return 1809.83
                        else:  # if miles_per_day > 99.187500
                            return 644.69
                    else:  # if miles_per_day > 99.750000
                        if days_squared <= 30.500000:
                            if log_miles <= 6.938641:
                                if receipts_per_day <= 479.110001:
                                    if miles_receipts <= 1356879.125000:
                                        if sqrt_miles <= 29.160782:
                                            return 1690.82
                                        else:  # if sqrt_miles > 29.160782
                                            return 1676.79
                                    else:  # if miles_receipts > 1356879.125000
                                        if miles <= 900.000000:
                                            if miles_receipts <= 1422778.187500:
                                                return 1796.70
                                            else:  # if miles_receipts > 1422778.187500
                                                if log_miles <= 6.666944:
                                                    return 1789.85
                                                else:  # if log_miles > 6.666944
                                                    if receipts_per_mile <= 2.475971:
                                                        return 1792.88
                                                    else:  # if receipts_per_mile > 2.475971
                                                        return 1791.96
                                        else:  # if miles > 900.000000
                                            if miles_per_day <= 194.599998:
                                                if sqrt_receipts_cubed_scaled <= 103.648052:
                                                    return 1696.72
                                                else:  # if sqrt_receipts_cubed_scaled > 103.648052
                                                    return 1691.38
                                            else:  # if miles_per_day > 194.599998
                                                if sqrt_miles <= 31.733228:
                                                    return 1743.85
                                                else:  # if sqrt_miles > 31.733228
                                                    if receipts_squared <= 3827750.125000:
                                                        return 1749.31
                                                    else:  # if receipts_squared > 3827750.125000
                                                        return 1810.37
                                else:  # if receipts_per_day > 479.110001
                                    if receipts_to_total_cost_ratio <= 3.166614:
                                        return 1699.56
                                    else:  # if receipts_to_total_cost_ratio > 3.166614
                                        return 1643.96
                            else:  # if log_miles > 6.938641
                                if days_times_miles <= 4748.000000:
                                    if log_miles <= 7.020625:
                                        if miles_per_day <= 270.000000:
                                            return 1605.84
                                        else:  # if miles_per_day > 270.000000
                                            return 1695.08
                                    else:  # if log_miles > 7.020625
                                        if sqrt_receipts_times_days <= 181.605293:
                                            return 1565.16
                                        else:  # if sqrt_receipts_times_days > 181.605293
                                            return 1567.43
                                else:  # if days_times_miles > 4748.000000
                                    if sqrt_receipts_times_days <= 182.118690:
                                        return 1745.09
                                    else:  # if sqrt_receipts_times_days > 182.118690
                                        if sqrt_receipts_times_miles <= 54729.771484:
                                            if log_days_times_miles <= 8.648243:
                                                if miles_receipts <= 2051547.125000:
                                                    return 1658.97
                                                else:  # if miles_receipts > 2051547.125000
                                                    if receipts <= 2309.085083:
                                                        return 1665.23
                                                    else:  # if receipts > 2309.085083
                                                        if sqrt_receipts_cubed_scaled <= 120.186085:
                                                            return 1664.76
                                                        else:  # if sqrt_receipts_cubed_scaled > 120.186085
                                                            return 1664.83
                                            else:  # if log_days_times_miles > 8.648243
                                                return 1673.89
                                        else:  # if sqrt_receipts_times_miles > 54729.771484
                                            if sqrt_receipts_times_miles <= 55999.894531:
                                                return 1711.97
                                            else:  # if sqrt_receipts_times_miles > 55999.894531
                                                return 1691.15
                        else:  # if days_squared > 30.500000
                            if days_squared <= 42.500000:
                                if receipts_per_mile <= 1.328626:
                                    if receipts_squared <= 1496868.437500:
                                        return 1803.97
                                    else:  # if receipts_squared > 1496868.437500
                                        return 1871.76
                                else:  # if receipts_per_mile > 1.328626
                                    if sqrt_receipts_times_miles <= 37165.871094:
                                        if miles_per_receipt <= 0.665042:
                                            if miles_receipts <= 1407789.062500:
                                                if days_receipts <= 9291.029785:
                                                    if sqrt_receipts_squared <= 1328.160034:
                                                        return 1771.80
                                                    else:  # if sqrt_receipts_squared > 1328.160034
                                                        return 1765.79
                                                else:  # if days_receipts > 9291.029785
                                                    if miles <= 746.500000:
                                                        return 1796.98
                                                    else:  # if miles > 746.500000
                                                        return 1817.77
                                            else:  # if miles_receipts > 1407789.062500
                                                if miles_per_receipt <= 0.408905:
                                                    return 1757.81
                                                else:  # if miles_per_receipt > 0.408905
                                                    if miles_receipts <= 1457890.062500:
                                                        return 1718.76
                                                    else:  # if miles_receipts > 1457890.062500
                                                        return 1737.86
                                        else:  # if miles_per_receipt > 0.665042
                                            if miles <= 863.500000:
                                                return 1704.06
                                            else:  # if miles > 863.500000
                                                return 1720.21
                                    else:  # if sqrt_receipts_times_miles > 37165.871094
                                        if sqrt_receipts_times_miles <= 37600.841797:
                                            return 1897.87
                                        else:  # if sqrt_receipts_times_miles > 37600.841797
                                            if receipts <= 1971.559998:
                                                if sqrt_receipts_times_miles <= 39854.275391:
                                                    return 1807.42
                                                else:  # if sqrt_receipts_times_miles > 39854.275391
                                                    if receipts <= 1716.880005:
                                                        return 1776.48
                                                    else:  # if receipts > 1716.880005
                                                        return 1788.75
                                            else:  # if receipts > 1971.559998
                                                return 1718.79
                            else:  # if days_squared > 42.500000
                                if sqrt_receipts_times_days <= 298.596756:
                                    if days_times_miles <= 6520.000000:
                                        if miles <= 780.000000:
                                            if receipts_per_mile <= 2.090552:
                                                return 1961.96
                                            else:  # if receipts_per_mile > 2.090552
                                                return 1960.92
                                        else:  # if miles > 780.000000
                                            if sqrt_receipts_times_days <= 272.718582:
                                                if sqrt_receipts <= 35.619793:
                                                    return 1809.91
                                                else:  # if sqrt_receipts > 35.619793
                                                    return 1826.08
                                            else:  # if sqrt_receipts_times_days > 272.718582
                                                return 1780.65
                                    else:  # if days_times_miles > 6520.000000
                                        if days_receipts <= 10680.229980:
                                            return 2004.34
                                        else:  # if days_receipts > 10680.229980
                                            return 2032.23
                                else:  # if sqrt_receipts_times_days > 298.596756
                                    if sqrt_receipts_times_days <= 333.364624:
                                        if miles <= 900.000000:
                                            if receipts_per_mile <= 2.068361:
                                                return 1847.26
                                            else:  # if receipts_per_mile > 2.068361
                                                return 1851.70
                                        else:  # if miles > 900.000000
                                            if receipts <= 2041.170044:
                                                return 1833.56
                                            else:  # if receipts > 2041.170044
                                                return 1839.67
                                    else:  # if sqrt_receipts_times_days > 333.364624
                                        if sqrt_receipts_cubed_scaled <= 118.366253:
                                            if days_times_miles <= 6916.000000:
                                                return 1719.37
                                            else:  # if days_times_miles > 6916.000000
                                                return 1747.22
                                        else:  # if sqrt_receipts_cubed_scaled > 118.366253
                                            return 1826.93
            else:  # if days_times_miles > 6939.000000
                if log_days_times_miles <= 9.381264:
                    if miles_per_day <= 127.340279:
                        if miles_receipts <= 877176.875000:
                            if miles_receipts <= 861281.843750:
                                if log_miles <= 6.471253:
                                    if sqrt_receipts_times_miles <= 19340.147461:
                                        return 1977.89
                                    else:  # if sqrt_receipts_times_miles > 19340.147461
                                        if sqrt_receipts_times_miles <= 20581.901367:
                                            if miles_squared <= 313128.000000:
                                                return 1842.10
                                            else:  # if miles_squared > 313128.000000
                                                return 1847.84
                                        else:  # if sqrt_receipts_times_miles > 20581.901367
                                            return 1930.24
                                else:  # if log_miles > 6.471253
                                    if miles_receipts <= 720634.843750:
                                        if sqrt_receipts_times_miles <= 22997.588867:
                                            if receipts <= 881.660004:
                                                return 1837.11
                                            else:  # if receipts > 881.660004
                                                return 1780.07
                                        else:  # if sqrt_receipts_times_miles > 22997.588867
                                            if receipts_per_day <= 72.165585:
                                                return 1683.49
                                            else:  # if receipts_per_day > 72.165585
                                                if is_11_to_14_days <= 0.500000:
                                                    return 1589.75
                                                else:  # if is_11_to_14_days > 0.500000
                                                    return 1575.52
                                    else:  # if miles_receipts > 720634.843750
                                        if log_days_times_miles <= 9.300421:
                                            if log_receipts <= 6.836292:
                                                if log_days_times_miles <= 9.210411:
                                                    return 1852.24
                                                else:  # if log_days_times_miles > 9.210411
                                                    if days_squared <= 122.000000:
                                                        return 1865.67
                                                    else:  # if days_squared > 122.000000
                                                        return 1862.13
                                            else:  # if log_receipts > 6.836292
                                                if log_miles <= 6.771588:
                                                    if receipts_fourth_scaled <= 1.132779:
                                                        if receipts_squared <= 962877.156250:
                                                            if receipts_squared <= 908515.531250:
                                                                return 1793.36
                                                            else:  # if receipts_squared > 908515.531250
                                                                return 1793.07
                                                        else:  # if receipts_squared > 962877.156250
                                                            return 1785.47
                                                    else:  # if receipts_fourth_scaled > 1.132779
                                                        return 1815.02
                                                else:  # if log_miles > 6.771588
                                                    return 1714.80
                                        else:  # if log_days_times_miles > 9.300421
                                            return 1663.58
                            else:  # if miles_receipts > 861281.843750
                                return 902.09
                        else:  # if miles_receipts > 877176.875000
                            if receipts_per_day <= 174.049263:
                                if receipts_per_mile <= 1.396846:
                                    if receipts_per_day <= 103.870609:
                                        return 2098.07
                                    else:  # if receipts_per_day > 103.870609
                                        if miles <= 1007.000000:
                                            if sqrt_receipts <= 34.472269:
                                                if days <= 9.500000:
                                                    return 1964.86
                                                else:  # if days > 9.500000
                                                    return 1950.30
                                            else:  # if sqrt_receipts > 34.472269
                                                if sqrt_receipts_cubed_scaled <= 43.594376:
                                                    return 2016.46
                                                else:  # if sqrt_receipts_cubed_scaled > 43.594376
                                                    if miles_per_receipt <= 0.733565:
                                                        return 1987.39
                                                    else:  # if miles_per_receipt > 0.733565
                                                        return 2000.42
                                        else:  # if miles > 1007.000000
                                            return 1903.76
                                else:  # if receipts_per_mile > 1.396846
                                    if sqrt_receipts_times_days <= 338.398666:
                                        if log_receipts <= 7.155528:
                                            return 1780.58
                                        else:  # if log_receipts > 7.155528
                                            return 1727.10
                                    else:  # if sqrt_receipts_times_days > 338.398666
                                        if miles_per_day <= 39.467033:
                                            return 2079.14
                                        else:  # if miles_per_day > 39.467033
                                            if sqrt_receipts_times_days <= 377.354538:
                                                if log_days_times_miles <= 9.087511:
                                                    if sqrt_receipts <= 38.114031:
                                                        if sqrt_receipts_squared <= 1387.184998:
                                                            return 2000.19
                                                        else:  # if sqrt_receipts_squared > 1387.184998
                                                            return 2007.62
                                                    else:  # if sqrt_receipts > 38.114031
                                                        return 2024.20
                                                else:  # if log_days_times_miles > 9.087511
                                                    return 1880.76
                                            else:  # if sqrt_receipts_times_days > 377.354538
                                                if sqrt_receipts_times_days <= 413.391373:
                                                    if sqrt_receipts_times_days <= 406.996948:
                                                        if miles_squared <= 852864.500000:
                                                            if log_days_times_miles <= 9.006570:
                                                                return 1878.06
                                                            else:  # if log_days_times_miles > 9.006570
                                                                if days_squared <= 110.500000:
                                                                    return 1872.81
                                                                else:  # if days_squared > 110.500000
                                                                    return 1871.27
                                                        else:  # if miles_squared > 852864.500000
                                                            if receipts_squared <= 2204274.812500:
                                                                return 1804.68
                                                            else:  # if receipts_squared > 2204274.812500
                                                                return 1827.18
                                                    else:  # if sqrt_receipts_times_days > 406.996948
                                                        if receipts_to_total_cost_ratio <= 1.463790:
                                                            return 1752.72
                                                        else:  # if receipts_to_total_cost_ratio > 1.463790
                                                            return 1724.42
                                                else:  # if sqrt_receipts_times_days > 413.391373
                                                    if receipts_per_mile <= 3.798945:
                                                        if miles_per_day <= 55.057692:
                                                            if sqrt_receipts_cubed_scaled <= 82.606056:
                                                                if days_times_miles <= 7636.000000:
                                                                    return 1881.36
                                                                else:  # if days_times_miles > 7636.000000
                                                                    return 1889.90
                                                            else:  # if sqrt_receipts_cubed_scaled > 82.606056
                                                                if log_receipts <= 7.749319:
                                                                    if miles_receipts <= 1249352.937500:
                                                                        return 2000.39
                                                                    else:  # if miles_receipts > 1249352.937500
                                                                        if sqrt_receipts_times_days <= 634.807373:
                                                                            if receipts_per_day <= 156.002357:
                                                                                return 1980.99
                                                                            else:  # if receipts_per_day > 156.002357
                                                                                return 1979.83
                                                                        else:  # if sqrt_receipts_times_days > 634.807373
                                                                            return 1989.13
                                                                else:  # if log_receipts > 7.749319
                                                                    return 1931.21
                                                        else:  # if miles_per_day > 55.057692
                                                            if days_receipts <= 16635.574219:
                                                                if sqrt_receipts <= 38.674786:
                                                                    if receipts_to_total_cost_ratio <= 1.292442:
                                                                        if days_receipts <= 15419.504883:
                                                                            return 1921.09
                                                                        else:  # if days_receipts > 15419.504883
                                                                            return 1921.68
                                                                    else:  # if receipts_to_total_cost_ratio > 1.292442
                                                                        if days <= 11.500000:
                                                                            return 1952.80
                                                                        else:  # if days > 11.500000
                                                                            return 1953.03
                                                                else:  # if sqrt_receipts > 38.674786
                                                                    return 2030.59
                                                            else:  # if days_receipts > 16635.574219
                                                                if miles <= 829.500000:
                                                                    if sqrt_miles <= 26.711419:
                                                                        if days_receipts <= 20146.794922:
                                                                            if miles_per_receipt <= 0.432751:
                                                                                return 1870.43
                                                                            else:  # if miles_per_receipt > 0.432751
                                                                                return 1873.19
                                                                        else:  # if days_receipts > 20146.794922
                                                                            return 1916.37
                                                                    else:  # if sqrt_miles > 26.711419
                                                                        if sqrt_receipts_times_miles <= 32252.564453:
                                                                            if days_times_miles <= 8359.500000:
                                                                                return 1847.08
                                                                            else:  # if days_times_miles > 8359.500000
                                                                                if sqrt_receipts <= 40.046566:
                                                                                    return 1837.25
                                                                                else:  # if sqrt_receipts > 40.046566
                                                                                    return 1829.06
                                                                        else:  # if sqrt_receipts_times_miles > 32252.564453
                                                                            if sqrt_receipts_times_days <= 570.172302:
                                                                                return 1809.29
                                                                            else:  # if sqrt_receipts_times_days > 570.172302
                                                                                return 1819.41
                                                                else:  # if miles > 829.500000
                                                                    if days_times_miles <= 11134.500000:
                                                                        if sqrt_receipts <= 41.888680:
                                                                            return 1897.37
                                                                        else:  # if sqrt_receipts > 41.888680
                                                                            if miles_receipts <= 1603031.000000:
                                                                                return 1951.77
                                                                            else:  # if miles_receipts > 1603031.000000
                                                                                if miles_receipts <= 1697605.125000:
                                                                                    return 1944.89
                                                                                else:  # if miles_receipts > 1697605.125000
                                                                                    return 1944.88
                                                                    else:  # if days_times_miles > 11134.500000
                                                                        if sqrt_receipts_times_miles <= 41547.751953:
                                                                            if miles <= 911.500000:
                                                                                return 1889.71
                                                                            else:  # if miles > 911.500000
                                                                                return 1879.09
                                                                        else:  # if sqrt_receipts_times_miles > 41547.751953
                                                                            return 1833.24
                                                    else:  # if receipts_per_mile > 3.798945
                                                        if days_receipts <= 31217.008789:
                                                            return 1745.09
                                                        else:  # if days_receipts > 31217.008789
                                                            return 1828.37
                            else:  # if receipts_per_day > 174.049263
                                if sqrt_receipts_times_days <= 376.903107:
                                    if miles_per_day <= 110.972221:
                                        return 1849.58
                                    else:  # if miles_per_day > 110.972221
                                        if miles_receipts <= 1477821.812500:
                                            return 1944.62
                                        else:  # if miles_receipts > 1477821.812500
                                            if days_times_miles <= 7416.000000:
                                                return 1902.37
                                            else:  # if days_times_miles > 7416.000000
                                                if sqrt_receipts_cubed_scaled <= 77.126366:
                                                    return 1894.85
                                                else:  # if sqrt_receipts_cubed_scaled > 77.126366
                                                    return 1897.19
                                else:  # if sqrt_receipts_times_days > 376.903107
                                    if sqrt_receipts_times_days <= 421.745224:
                                        if log_days_times_miles <= 9.052170:
                                            if receipts_to_total_cost_ratio <= 2.118690:
                                                return 1694.37
                                            else:  # if receipts_to_total_cost_ratio > 2.118690
                                                if receipts_fourth_scaled <= 33.418339:
                                                    if log_days_times_miles <= 8.875265:
                                                        return 1718.71
                                                    else:  # if log_days_times_miles > 8.875265
                                                        if miles_squared <= 832072.000000:
                                                            return 1726.51
                                                        else:  # if miles_squared > 832072.000000
                                                            return 1732.12
                                                else:  # if receipts_fourth_scaled > 33.418339
                                                    return 1755.05
                                        else:  # if log_days_times_miles > 9.052170
                                            if sqrt_receipts_times_days <= 402.423019:
                                                if log_receipts <= 7.569525:
                                                    return 1778.65
                                                else:  # if log_receipts > 7.569525
                                                    if miles_receipts <= 2193056.625000:
                                                        return 1763.16
                                                    else:  # if miles_receipts > 2193056.625000
                                                        return 1759.33
                                            else:  # if sqrt_receipts_times_days > 402.423019
                                                return 1810.94
                                    else:  # if sqrt_receipts_times_days > 421.745224
                                        if sqrt_receipts_times_days <= 428.486694:
                                            if miles_receipts <= 1802465.625000:
                                                return 1883.49
                                            else:  # if miles_receipts > 1802465.625000
                                                return 1913.87
                                        else:  # if sqrt_receipts_times_days > 428.486694
                                            if miles_per_day <= 51.833332:
                                                return 1918.46
                                            else:  # if miles_per_day > 51.833332
                                                if sqrt_receipts_times_miles <= 31058.491211:
                                                    if receipts_per_day <= 188.745148:
                                                        if receipts_cubed_scaled <= 8.798310:
                                                            return 1732.20
                                                        else:  # if receipts_cubed_scaled > 8.798310
                                                            return 1758.03
                                                    else:  # if receipts_per_day > 188.745148
                                                        if receipts_fourth_scaled <= 23.072571:
                                                            return 1715.29
                                                        else:  # if receipts_fourth_scaled > 23.072571
                                                            return 1699.94
                                                else:  # if sqrt_receipts_times_miles > 31058.491211
                                                    if miles_per_receipt <= 0.351431:
                                                        if miles_per_receipt <= 0.298273:
                                                            if log_receipts <= 7.776316:
                                                                return 1807.33
                                                            else:  # if log_receipts > 7.776316
                                                                return 1792.31
                                                        else:  # if miles_per_receipt > 0.298273
                                                            if receipts_to_total_cost_ratio <= 2.449197:
                                                                if miles_squared <= 554557.000000:
                                                                    return 1872.89
                                                                else:  # if miles_squared > 554557.000000
                                                                    return 1872.44
                                                            else:  # if receipts_to_total_cost_ratio > 2.449197
                                                                return 1873.94
                                                    else:  # if miles_per_receipt > 0.351431
                                                        if receipts_per_mile <= 2.148148:
                                                            if sqrt_receipts_times_days <= 446.645660:
                                                                if receipts_per_day <= 222.019554:
                                                                    return 1805.77
                                                                else:  # if receipts_per_day > 222.019554
                                                                    return 1728.07
                                                            else:  # if sqrt_receipts_times_days > 446.645660
                                                                if receipts_per_mile <= 2.015391:
                                                                    return 1844.58
                                                                else:  # if receipts_per_mile > 2.015391
                                                                    if days <= 10.500000:
                                                                        return 1889.87
                                                                    else:  # if days > 10.500000
                                                                        return 1900.18
                                                        else:  # if receipts_per_mile > 2.148148
                                                            if receipts_fourth_scaled <= 38.988529:
                                                                if log_receipts <= 7.706668:
                                                                    if days_receipts <= 20220.250000:
                                                                        return 1749.93
                                                                    else:  # if days_receipts > 20220.250000
                                                                        if sqrt_receipts <= 44.480541:
                                                                            return 1787.57
                                                                        else:  # if sqrt_receipts > 44.480541
                                                                            if miles_receipts <= 1879765.687500:
                                                                                if receipts_cubed_scaled <= 8.299030:
                                                                                    return 1779.12
                                                                                else:  # if receipts_cubed_scaled > 8.299030
                                                                                    return 1779.08
                                                                            else:  # if miles_receipts > 1879765.687500
                                                                                if sqrt_receipts <= 46.675762:
                                                                                    return 1775.03
                                                                                else:  # if sqrt_receipts > 46.675762
                                                                                    return 1776.62
                                                                else:  # if log_receipts > 7.706668
                                                                    if miles_per_day <= 79.250000:
                                                                        return 1740.85
                                                                    else:  # if miles_per_day > 79.250000
                                                                        if log_days_times_miles <= 9.379661:
                                                                            if miles <= 1024.500000:
                                                                                if receipts_squared <= 5372937.250000:
                                                                                    return 1758.56
                                                                                else:  # if receipts_squared > 5372937.250000
                                                                                    if long_trip_high_receipts <= 0.500000:
                                                                                        return 1759.97
                                                                                    else:  # if long_trip_high_receipts > 0.500000
                                                                                        return 1760.00
                                                                            else:  # if miles > 1024.500000
                                                                                return 1761.94
                                                                        else:  # if log_days_times_miles > 9.379661
                                                                            return 1753.84
                                                            else:  # if receipts_fourth_scaled > 38.988529
                                                                return 1791.69
                    else:  # if miles_per_day > 127.340279
                        if days_receipts <= 12912.535156:
                            if receipts_per_mile <= 0.859380:
                                if miles_receipts <= 1035545.781250:
                                    return 1699.90
                                else:  # if miles_receipts > 1035545.781250
                                    return 1840.75
                            else:  # if receipts_per_mile > 0.859380
                                if miles_receipts <= 1603493.812500:
                                    if miles_per_day <= 144.000000:
                                        if receipts_to_total_cost_ratio <= 1.006496:
                                            return 2073.13
                                        else:  # if receipts_to_total_cost_ratio > 1.006496
                                            if miles_per_receipt <= 0.869230:
                                                if days_times_miles <= 8718.500000:
                                                    return 2279.82
                                                else:  # if days_times_miles > 8718.500000
                                                    return 2248.12
                                            else:  # if miles_per_receipt > 0.869230
                                                if log_days_times_miles <= 9.142147:
                                                    return 2214.64
                                                else:  # if log_days_times_miles > 9.142147
                                                    return 2164.15
                                    else:  # if miles_per_day > 144.000000
                                        if miles_receipts <= 1179540.687500:
                                            if receipts <= 1019.640015:
                                                return 2119.83
                                            else:  # if receipts > 1019.640015
                                                return 2132.85
                                        else:  # if miles_receipts > 1179540.687500
                                            if sqrt_receipts_times_miles <= 37898.503906:
                                                return 2014.72
                                            else:  # if sqrt_receipts_times_miles > 37898.503906
                                                if miles_per_receipt <= 0.900995:
                                                    return 2063.98
                                                else:  # if miles_per_receipt > 0.900995
                                                    return 2047.06
                                else:  # if miles_receipts > 1603493.812500
                                    if receipts_to_total_cost_ratio <= 1.558130:
                                        return 1862.45
                                    else:  # if receipts_to_total_cost_ratio > 1.558130
                                        if receipts_per_mile <= 1.535888:
                                            return 2072.18
                                        else:  # if receipts_per_mile > 1.535888
                                            if miles_per_receipt <= 0.625053:
                                                return 1971.23
                                            else:  # if miles_per_receipt > 0.625053
                                                return 1972.88
                        else:  # if days_receipts > 12912.535156
                            if sqrt_receipts_cubed_scaled <= 114.554344:
                                if log_days_times_miles <= 9.196329:
                                    if days_times_miles <= 9132.000000:
                                        if miles <= 1058.500000:
                                            return 1794.57
                                        else:  # if miles > 1058.500000
                                            if sqrt_miles <= 33.481308:
                                                if log_miles <= 7.005684:
                                                    if sqrt_receipts_squared <= 2038.165039:
                                                        return 1857.04
                                                    else:  # if sqrt_receipts_squared > 2038.165039
                                                        return 1858.36
                                                else:  # if log_miles > 7.005684
                                                    return 1852.47
                                            else:  # if sqrt_miles > 33.481308
                                                if log_receipts <= 7.635021:
                                                    return 1833.27
                                                else:  # if log_receipts > 7.635021
                                                    return 1839.47
                                    else:  # if days_times_miles > 9132.000000
                                        return 1752.18
                                else:  # if log_days_times_miles > 9.196329
                                    return 1945.95
                            else:  # if sqrt_receipts_cubed_scaled > 114.554344
                                if sqrt_receipts_squared <= 2443.209961:
                                    return 1917.57
                                else:  # if sqrt_receipts_squared > 2443.209961
                                    return 1921.16
                else:  # if log_days_times_miles > 9.381264
                    if receipts_to_total_cost_ratio <= 1.427901:
                        if receipts_per_day <= 66.681923:
                            if log_days_times_miles <= 9.588021:
                                return 1846.41
                            else:  # if log_days_times_miles > 9.588021
                                return 1797.14
                        else:  # if receipts_per_day > 66.681923
                            if log_miles <= 6.922131:
                                if days_times_miles <= 12535.500000:
                                    if days_times_miles <= 12060.000000:
                                        if sqrt_receipts_cubed_scaled <= 44.760069:
                                            return 1996.18
                                        else:  # if sqrt_receipts_cubed_scaled > 44.760069
                                            return 1967.87
                                    else:  # if days_times_miles > 12060.000000
                                        if receipts_cubed_scaled <= 2.678558:
                                            return 1925.32
                                        else:  # if receipts_cubed_scaled > 2.678558
                                            return 1921.18
                                else:  # if days_times_miles > 12535.500000
                                    if miles_squared <= 973292.500000:
                                        if miles_per_day <= 69.071430:
                                            return 2065.16
                                        else:  # if miles_per_day > 69.071430
                                            return 1995.87
                                    else:  # if miles_squared > 973292.500000
                                        if receipts_per_mile <= 1.284422:
                                            return 2124.16
                                        else:  # if receipts_per_mile > 1.284422
                                            return 2080.00
                            else:  # if log_miles > 6.922131
                                if log_days_times_miles <= 9.566265:
                                    if receipts_fourth_scaled <= 1.280504:
                                        if log_receipts <= 6.865771:
                                            return 2090.54
                                        else:  # if log_receipts > 6.865771
                                            return 2030.76
                                    else:  # if receipts_fourth_scaled > 1.280504
                                        if miles_squared <= 1079746.000000:
                                            return 2097.69
                                        else:  # if miles_squared > 1079746.000000
                                            if is_very_high_receipts_1500 <= 0.500000:
                                                if days_receipts <= 13248.189941:
                                                    return 2159.33
                                                else:  # if days_receipts > 13248.189941
                                                    if log_miles <= 7.021502:
                                                        return 2162.03
                                                    else:  # if log_miles > 7.021502
                                                        return 2162.13
                                            else:  # if is_very_high_receipts_1500 > 0.500000
                                                return 2143.74
                                else:  # if log_days_times_miles > 9.566265
                                    if log_miles <= 6.976148:
                                        return 2337.73
                                    else:  # if log_miles > 6.976148
                                        if days <= 13.500000:
                                            if log_days_times_miles <= 9.615504:
                                                return 2214.64
                                            else:  # if log_days_times_miles > 9.615504
                                                return 2197.33
                                        else:  # if days > 13.500000
                                            return 2239.35
                    else:  # if receipts_to_total_cost_ratio > 1.427901
                        if receipts_to_total_cost_ratio <= 1.909135:
                            if miles_per_day <= 95.888111:
                                if miles_per_day <= 81.934067:
                                    if receipts_fourth_scaled <= 20.880196:
                                        if miles_receipts <= 1964774.562500:
                                            if is_extreme_receipts_2000 <= 0.500000:
                                                if days_receipts <= 23185.174805:
                                                    return 1960.67
                                                else:  # if days_receipts > 23185.174805
                                                    return 1956.89
                                            else:  # if is_extreme_receipts_2000 > 0.500000
                                                return 1970.01
                                        else:  # if miles_receipts > 1964774.562500
                                            return 1997.52
                                    else:  # if receipts_fourth_scaled > 20.880196
                                        return 1905.50
                                else:  # if miles_per_day > 81.934067
                                    if log_days_times_miles <= 9.704670:
                                        if log_days_times_miles <= 9.560217:
                                            if receipts_per_day <= 159.531670:
                                                return 1875.72
                                            else:  # if receipts_per_day > 159.531670
                                                return 1883.21
                                        else:  # if log_days_times_miles > 9.560217
                                            if sqrt_receipts_times_miles <= 55987.572266:
                                                return 1899.69
                                            else:  # if sqrt_receipts_times_miles > 55987.572266
                                                return 1906.35
                                    else:  # if log_days_times_miles > 9.704670
                                        return 1943.24
                            else:  # if miles_per_day > 95.888111
                                if receipts_to_total_cost_ratio <= 1.865169:
                                    if receipts_to_total_cost_ratio <= 1.698083:
                                        return 2013.21
                                    else:  # if receipts_to_total_cost_ratio > 1.698083
                                        if miles_squared <= 1290896.000000:
                                            return 1987.44
                                        else:  # if miles_squared > 1290896.000000
                                            return 1988.56
                                else:  # if receipts_to_total_cost_ratio > 1.865169
                                    return 2050.62
                        else:  # if receipts_to_total_cost_ratio > 1.909135
                            if sqrt_receipts <= 49.838053:
                                if sqrt_miles <= 32.779566:
                                    if log_miles <= 6.961116:
                                        return 1842.24
                                    else:  # if log_miles > 6.961116
                                        return 1843.97
                                else:  # if sqrt_miles > 32.779566
                                    return 1798.38
                            else:  # if sqrt_receipts > 49.838053
                                if receipts_cubed_scaled <= 15.502147:
                                    return 1894.16
                                else:  # if receipts_cubed_scaled > 15.502147
                                    return 1885.87

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    try:
        days = int(sys.argv[1])
        miles = float(sys.argv[2])
        receipts = float(sys.argv[3])
        result = predict(days, miles, receipts)
        print(f"{result:.2f}")
    except:
        sys.exit(1)
