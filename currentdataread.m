% close all
 %clear all
%filename='C:\Users\RAISSA\Documents\MATLAB\wave_current\Dados Brutos\2.PC_julho_2011\PC_31.07.2011_2\chd202.dat';
function [E,V]=currentdataread(filename)
fid = fopen(filename);
E=[];
V=[];
j=0;
while ~feof(fid)
    j=j+1;
    dum1 = textscan(fid,'%f', 19);
    data1 = cell2mat(dum1);
        if ~isempty(data1)
        E=[E;data1'];
        n_celdas=data1(19);
            for i=1:n_celdas
            dum2 = textscan(fid,'%f', 10);
            data2(i,:) = cell2mat(dum2);
            end
    V(:,:,j)=data2;
    else
        disp('fin del archivo')
        break
    end
end

fclose(fid);
return