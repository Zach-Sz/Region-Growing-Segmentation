% Region Growing
% Date: October 24, 2019
% By: Zachary Szentimrey and Nicholas Belanger
% Dscription: Performs a region growing segmentation algorithm. User inputs
% a given number of seeds and a threshold value for the algorithm as well
% as the image to segment.


% Import image
image = rgb2gray(imread('WorldMap.png')); %change to 'WorldMap.png' for image 2 and 'segbreak.png' for image 1
threshold = 10; %user to set the threshold value
seed = [335;950]; %user to define the seed point(s) [vertical;horizontal]

% Calls the region_grow function which performs the entire region growing
% segmentation. tic toc is used to show the length of time of the
% implementation (for efficiency purposes).
tic
segimage = region_grow(image,seed,threshold);
imshow(segimage) % show resultant segmented image
toc



% Performs the actualy comparison between the current pixel you are at and
% the pixel beside you. It also ensure you don't try and access pixels
% outside of the image (edge cases) and adds the pixel you used to the list
% of used pixels. Additionally, it adds the pixel beside you to the list of
% pixels to analyze.
function [pixelxy, segimg] = run_loop(x,y,threshold,segimg,orimg, pixelxy, B, A, used)
    if pixelxy(2,1)+1 < B+1 && pixelxy(2,1)-1 >= 1 &&  pixelxy(1,1)-1 >=1 && pixelxy(1,1)+1 < A+1 %ensure you access only pixels inside your image
        if abs(double(orimg(pixelxy(1,1),pixelxy(2,1))) - double(orimg(pixelxy(1,1)+x,pixelxy(2,1)+y)))< threshold %performs the actual comparison between the difference of the current with adjacent pixel and the threshold
            segimg(pixelxy(1,1)+x,pixelxy(2,1)+y) = 255; %if within the threshold, the pixel besides value is changed to be included in the segmented image
            if sum(pixelxy(1, :) == pixelxy(1,1)+x & pixelxy(2, :) == pixelxy(2,1)+y) == 0 && sum(used(1, :) == pixelxy(1,1)+x & used(2, :) == pixelxy(2,1)+y) == 0 %checks to see if the pixel beside you is already used or in the list of pixels to analyze
                pix = [pixelxy(1,1)+x;pixelxy(2,1)+y];
                pixelxy = [pixelxy,pix]; %adds pixel beside you to the list of pixels to analyze (compare)
            end
        end
    end
end

% region_grow function which accepst the original image, seed(s) and
% threshold value and returns the segmented image
function [segimg] = region_grow(orimg, seed, threshold)
    [A,B] = size(orimg); %calculates the image size (height vs. width)
    segimg = zeros(A,B); %initializes blank segmented image
    segimg(seed(1,:),seed(2,:)) = 255; %places seed(s) on segmented image
    pixelxy = seed; %pixelxy is the list of pixels to analyze
    used = seed; %list of pixels that you have already analyzed.
    
    % Performs the region growing as long as you have pixel to compare (the
    % pixelxy list is not empty)
    while length(pixelxy) > 0
        % Four lines below are for the 4 neighbourhood comparison. Each of
        % them calls the run_loop function which performs the comparison
        % between the current pixels and the threshold
        [pixelxy,segimg] = run_loop(0,1,threshold,segimg,orimg, pixelxy, B, A, used); %compares current pixel with the one to the right
        [pixelxy,segimg] = run_loop(0,-1,threshold,segimg,orimg, pixelxy, B, A, used); %compares current pixel with the one to the left
        [pixelxy,segimg] = run_loop(1,0,threshold,segimg,orimg, pixelxy, B, A, used); %compares current pixel with the one above
        [pixelxy,segimg] = run_loop(-1,0,threshold,segimg,orimg, pixelxy, B, A, used); %compares current pixel with the one below
        
        % Four below lines are for the corner pixels (to make it 8
        % neighbourhood
        [pixelxy,segimg] = run_loop(1,1,threshold,segimg,orimg, pixelxy, B, A, used); %compares current pixel with the one top-right
        [pixelxy,segimg] = run_loop(1,-1,threshold,segimg,orimg, pixelxy, B, A, used); %compares current pixel with the one top-left
        [pixelxy,segimg] = run_loop(-1,-1,threshold,segimg,orimg, pixelxy, B, A, used); %compares current pixel with the one bottom-left
        [pixelxy,segimg] = run_loop(-1,1,threshold,segimg,orimg, pixelxy, B, A, used); %compares current pixel with the one bottom-right
        
        pixx = [pixelxy(1,1);pixelxy(2,1)]; %sets pixx to be the current pixel you looked at
        used = [used,pixx]; %adds the pixel you just analyzed to the list of used pixels
        pixelxy(:,1)=[]; %pops the first pixel index in the array (removes the pixel you just looked at from the list of pixels)
        
    end
end


