#include "stdio.h"

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

unsigned char* greyScale(unsigned char* image, int height, int width, int channels);
unsigned char* convertToAscii(unsigned char* image, int height, int width, int channels, int isColored);


int main()
{
    //Loads in Image data
    int width, height, channels;
    unsigned char *img = stbi_load("mcdonalds.png", &width, &height, &channels, 0);
    

    unsigned char *asciiImage = convertToAscii(img, height, width, channels, 0);

    //printf("%s\n", asciiImage);

    unsigned char* new_img = greyScale(img, height, width, channels);

    stbi_write_bmp("output.bmp", width, height, 1, new_img);
    //printf("%d ", new_channels);

    free(new_img);
    stbi_image_free(img);
}

unsigned char* convertToAscii(unsigned char* image, int height, int width, int channels, int isColored)
{
    //Creates new image array
    int new_channels = 1;
    unsigned char *new_img = (unsigned char*)malloc(width * height * sizeof(unsigned char) * new_channels);

    char lightArray[] = " `^\\\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$";
    long int lightArrayLen = sizeof(lightArray) / sizeof(char) - 1;


    new_img = greyScale(image, height, width, channels);
    
    for(int i = 0;  i < width * height ; i++)
    {
        //Grabs and sets all RGB values for chat
        unsigned char R, G, B;
        R = image[i * channels + 0];
        G = image[i * channels + 1];
        B = image[i * channels + 2];

        //Outputs cooresponding charcter to  in Cooresponding Color
        printf("\033[38;2;%d;%d;%dm%c\033[0m", R, G, B, lightArray[(int) new_img[i] * lightArrayLen / 256]);
        //printf("%c", lightArray[(int) new_img[i] * lightArrayLen / 256]);
        if (i % width - 1 == 0)
        {
            printf("\n");
        }
    }
    return new_img;
}

unsigned char* greyScale(unsigned char* image, int height, int width, int channels)
{
    unsigned char *new_img = (unsigned char*)malloc(width * height * sizeof(unsigned char));

    for (int i = 0;  i < height * width; i++)
    {
        //Gets Average Sum of image
        int sum = 0;

        for(int j = 0;  j < channels; j++)
        {sum += image[ channels * i + j];}

        sum = sum / channels;

        new_img[i] = sum;
    }

    return new_img;
}
