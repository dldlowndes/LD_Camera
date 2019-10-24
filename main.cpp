#include "LD_Camera.h"

#include <string>

int main(){
    LD_Camera::CameraOptions my_Options;

    // 0 = first available camera.
    my_Options.Camera_ID = 0;

    // Exposure etc data in form {pixel clock, frame rate, exposure(ms)}
    my_Options.exposure_Full = {36, 20, 50};
    // As above but for when the AOI is set.
    my_Options.exposure_AOI = {36, 50, 10};
    // Mode for the camera. This software stores everything as 16 bit but
    // this tells the hardware what data to output.
    my_Options.bits_Per_Pixel = 8;
    // Position is defined as top left of the AOI.
    my_Options.aoi_Dimensions.aoi_Position = {0, 0};
    my_Options.aoi_Dimensions.aoi_Size = {256, 256};

    LD_Camera::Camera my_Camera(my_Options);
    my_Camera.Take_Picture();
    my_Camera.Save_Picture("test_image.bin", true);

    return 0;
}
