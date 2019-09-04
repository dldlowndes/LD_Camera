#include "davecamera2.h"

#include <string>

int main(){
    DaveCamera2::CameraOptions my_Options;
    my_Options.Camera_ID = 0;
    my_Options.exposure_Full = {36, 20, 15};
    my_Options.exposure_AOI = {36, 50, 15};
    my_Options.bits_Per_Pixel = 10;
    my_Options.aoi_Dimensions.aoi_Position = {0, 0};
    my_Options.aoi_Dimensions.aoi_Size = {256, 256};

    Test_AOI(my_Options);
    return 0;
}
