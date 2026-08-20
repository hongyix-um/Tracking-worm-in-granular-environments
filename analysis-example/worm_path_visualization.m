clear
close all
clc

%% particle information
mdia = 20;
s_rad = 5;

%% 
% datapath = './plastic_beads/Trial3_data';
% dpath = dir(datapath);
% dpath(1:2) = [];

datapath = './plastic_beads/Trial3_data';
dpath = dir(datapath);
dpath(1:2) = [];

data_subsets = [3];

good_range = [10, 1850; 2050 3340]; % trial 3

%%
for id = data_subsets
    % id = 1;
    savepath = fullfile(datapath,dpath(id).name)
    predict_folder = fullfile(savepath,'images');
    % result_folder = fullfile(savepath,'predictions');
    % wormimg_folder = fullfile(savepath,'worm_images');
    % read the modified position with worm's position
    T = readtable(fullfile(savepath,'raw_data.csv'),'NumHeaderLines',1);
    result_folder = fullfile(savepath,'predictions');
    wormimg_folder = fullfile(savepath,'worm_images');

    T_index = 1:13;
    T_mat=table2array(T(:,T_index));
    T_mat(:,1) = T_mat(:,1)+1;

    imnames = dir(predict_folder);
    imnames(1:2) = [];
    len = length(imnames);

    particles = cell(len,1);
    
    % head_pos = [1 1];
    % flip_flag = zeros(len,2); % [flip head, multiple worm]

    %%

    % debug_frames = [2180:2220]
    debug_frames = [];

    flip_flag = readmatrix(fullfile(savepath,'flip_flag.dat'));

    % for i = 10:10:(len*10)

    head_collect = [];

    for i = 10:10:680

        idx = i/10;
        i

        if i==680
            imagename = sprintf('%d.tif',i);
            im = imread(fullfile(predict_folder,imagename));

            prefix = [];
            imagename_s = sprintf([prefix,'%d_binarized.png'],i);
            im_result = imread(fullfile(result_folder,imagename_s));
            imagename_worm = sprintf('_%d.tif',i);
            im_worm = imread(fullfile(wormimg_folder,imagename_worm));
            im_worm = rgb2gray(im_worm);

            figure(1)
            % imshowpair(im,im_worm)
            RGB = cat(3, 0.1*im_worm+im+0.65*im_result,0.05*im_result+im+im_worm*0.05,im+0.25*im_result+im_worm*0.85);
            % combined = imshowpair(im, im_worm, 'falsecolor'); 
            % imshowpair(combined, im_result, 'diff');
            imshow(RGB)
            hold on
            titlename = sprintf("frame %d",i);
            title(titlename)
        end
        

        trackID = find(T_mat(:,1)==i);
        T_i = T_mat(trackID,:);

        num_worms = size(T_i,1);
        

        if num_worms == 1

            j = 1;
            WlistX = [4,6,8,10,12];
            WlistY = [3,5,7,9,11];
            if flip_flag(idx,1) == 1
                 WlistX = fliplr(WlistX);
                 WlistY = fliplr(WlistY);
            end

            X_pos = T_i(j,WlistX);
            Y_pos = T_i(j,WlistY);

            head_collect = [head_collect ; [X_pos(3) Y_pos(3)]];
            if i==680
              plot(X_pos,Y_pos,'o k','markerfacecolor','y','MarkerSize',10,'LineWidth',2.0)
              plot(X_pos(1),Y_pos(1),'o k','markerfacecolor','r','MarkerSize',10,'LineWidth',2.0) 
              plot(X_pos(3),Y_pos(3),'o k','markerfacecolor','b','MarkerSize',10,'LineWidth',2.0) 
            end

            % titlename = sprintf("frame %d",i);
            % titlename = append(dpath(id).name, titlename);
            % text(50,50,titlename,'fontsize',16,'Color','w')
            % title(titlename)
            % hold off   
            % frame = getframe(gcf); % Capture the current figure
            % writeVideo(v, frame);  % Write to video

        end


    end

    plot(head_collect(:,1),head_collect(:,2),'- b','LineWidth',2.0)

    % close(v)
    % writematrix(flip_flag,fullfile(savepath,'flip_flag.dat'));

    %%

end

% writematrix(worm_density,'trial_4.dat');