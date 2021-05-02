clear, clc, close all


pfadcp = 0;

pathname = ('C:\Users\douglas.MENTAWAII\Documents\18 05-08\ADCP\ADCP_REEF_05-08-2015.wad');

%pathname_adv = ('C:\Users\douglas.MENTAWAII\Documents\18 05-08\ADV\ADV_RESERVA05_08_2015.dat');

dd = load(pathname);
%adv = load(pathname_adv);

%ADV
%coletou 1800 pontos
%freq am = 2 hz ??
%tempo de amost: 1024 ??

%seleciona dados do ADV por burst

%colcoar pressao corrigida na matriz do adv
% adv(:,15) = adv(:,15) - smooth(adv(:,15),3000);
% 
% %ultimo burst ADV
% ub = adv(end,1);
% 
% for c = 1:2:ub-2
%     
%     prdv(:,c) = adv(find(adv(:,1)==c),15);
%     vxdv(:,c) = adv(find(adv(:,1)==c),3);
%     vydv(:,c) = adv(find(adv(:,1)==c),4);
%     vzdv(:,c) = adv(find(adv(:,1)==c),5);
%     
%     
%     [f,an,anx,any,a1,b1,diraz,dirm,dirtp,fp,tp,hm0]=onda_freq(1,1000,prdv(:,c),vxdv(:,c),vydv(:,c));
%     
%     
% %     figure
% %     subplot(2,1,1)
% %     plot(f,an,'-o')
% %     title('ADV - pr')
% %     grid
% %     subplot(2,1,2)
% %     plot(f,diraz,'-o')
% %     grid
% 
%     [f,an,anx,any,a1,b1,diraz,dirm,dirtp,fp,tp,hm0]=onda_freq(0.5,1000,vzdv(:,c),vxdv(:,c),vydv(:,c));
% 
%     figure
%     subplot(2,1,1)
%     plot(f,an,'-o')
%     title('ADV - vz')
%     grid
%     subplot(2,1,2)
%     plot(f,diraz,'-o')
%     ylim([0,360])
%     grid
% 
%     
% 
% end
    
    
%ADCP
%cada burst tem 2048 pontos em 2 Hz (dt = 0.5)

c = 0;
for i = 1:2048:length(dd)
    
    c = c + 1;
    pr(:,c) = dd(i:i+2047,3);
    vx(:,c) = dd(i:i+2047,6);
    vy(:,c) = dd(i:i+2047,7);
    vz(:,c) = dd(i:i+2047,8);
    
%     [f,an,anx,any,a1,b1,diraz,dirm,dirtp,fp,tp,hm0]=onda_freq(0.5,1000,smooth(pr(:,c),10),vx(:,c),vy(:,c));
%     
%     
%     figure
%     subplot(2,1,1)
%     plot(f,an,'-o')
%     title('ADCP - pr')
%     grid
%     subplot(2,1,2)
%     plot(f,diraz,'-o')
%     grid

    [f,an,anx,any,a1,b1,diraz,dirm,dirtp,fp,tp,hm0]=onda_freq(0.5,1000,vz(:,c),vx(:,c),vy(:,c));

    figure
    subplot(2,1,1)
    plot(f,an,'-o')
    title('ADCP - vz')
    grid
    subplot(2,1,2)
    plot(f,diraz,'-o')
    ylim([0,360])
    grid

end
% 
% f = 1;
% figure
% plot(pr(:,f)-mean(pr(:,f)),'b')
% hold on
% plot(prdv(:,f)-mean(prdv(:,f)),'r')


