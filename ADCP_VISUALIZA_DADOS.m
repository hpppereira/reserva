clear all, close all, clc
%% Observa��o dos dados do ADCP Aquadopp
%Douglas NEMES
%Praia da Reserva
%ADCP AQUADOP NORTEK


% ARQUIVO.sen
%  1   Month                            (1-12)
%  2   Day                              (1-31)
%  3   Year
%  4   Hour                             (0-23)
%  5   Minute                           (0-59)
%  6   Second                           (0-59)
%  7   Error code
%  8   Status code
%  9   Battery voltage                  (V)
% 10   Soundspeed                       (m/s)
% 11   Heading                          (degrees)
% 12   Pitch                            (degrees)
% 13   Roll                             (degrees)
% 14   Pressure                         (dbar)
% 15   Temperature                      (degrees C)
% 16   Analog input 1
% 17   Analog input 2

load ('ADCP_05_08_2015.sen')
Dados_SEN = ADCP_05_08_2015
E_C = Dados_SEN(:,7);
figure(1)
subplot(5,1,1)
plot(E_C)
title ('Error Code')

Heading= Dados_SEN(:,11);
subplot(5,1,2)
plot(Heading)
title ('Heading')

Pitch = Dados_SEN(:,12);
subplot(5,1,3)
plot(Pitch )
title ('Pitch ')

Roll = Dados_SEN(:,13);
subplot(5,1,4)
plot(Roll)
title ('Roll')

Press_Sen = Dados_SEN(:,14);
subplot(5,1,5)
plot(Press_Sen)
title ('Press�o')


%%
% ARQUIVO.whd
%  1   Month                            (1-12)
%  2   Day                              (1-31)
%  3   Year
%  4   Hour                             (0-23)
%  5   Minute                           (0-59)
%  6   Second                           (0-59)
%  7   Burst counter
%  8   No of wave data records
%  9   Cell position                    (m)
% 10   Battery voltage                  (V)
% 11   Soundspeed                       (m/s)
% 12   Heading                          (degrees)
% 13   Pitch                            (degrees)
% 14   Roll                             (degrees)
% 15   Minimum pressure                 (dbar)
% 16   Maximum pressure                 (dbar)
% 17   Temperature                      (degrees C)
% 18   CellSize                         (m)
% 19   Noise amplitude beam 1           (counts)
% 20   Noise amplitude beam 2           (counts)
% 21   Noise amplitude beam 3           (counts)
% 22   Noise amplitude beam 4           (counts)
% 23   AST window start                 (m)
% 24   AST window size                  (m)
% 25   AST window offset                (m)

load ('ADCP_05_08_2015.whd');
Dados_whd = ADCP_05_08_2015;
Amp_1 = Dados_whd (:,19);
figure(2)
subplot(3,1,1)
plot(Amp_1 )
title (' Noise amplitude beam 1')

Amp_2 = Dados_whd (:,20);
subplot(3,1,2)
plot(Amp_2)
title ('Noise amplitude beam 2')

Amp_3 = Dados_whd (:,21);
subplot(3,1,3)
plot(Amp_3)
title ('Noise amplitude beam 3 ')




%%
% ARQUIVO.wad
%  1   Burst counter
%  2   Ensemble counter
%  3   Pressure                         (dbar)
%  4   Spare
%  5   Analog input
%  6   Velocity (Beam1|X|East)          (m/s)
%  7   Velocity (Beam2|Y|North)         (m/s)
%  8   Velocity (Beam3|Z|Up)            (m/s)
%  9   Velocity (N/A)                   (m/s)
% 10   Amplitude (Beam1)                (counts)
% 11   Amplitude (Beam2)                (counts)
% 12   Amplitude (Beam3)                (counts)
% 13   Amplitude (N/A)                  (counts)


load ('ADCP_05_08_2015.wad');
Dados_wad = ADCP_05_08_2015;
%Error Code
PressWad = Dados_wad (:,3);
figure(3)
subplot(4,1,1)
plot(PressWad)
title ('Press�o .wad')

Vx_E = Dados_wad (:,6);
subplot(4,1,2)
plot(Vx_E)
title ('Velocity (Beam1|X|East) m/s')

Vy_N = Dados_wad (:,7);
subplot(4,1,3)
plot(Vy_N )
title ('Velocity (Beam2|Y|North) m/s ')

Vz_up = Dados_wad (:,8);
subplot(4,1,4)
plot(Vz_up)
title (' Velocity (Beam3|Z|Up) m/s')

figure(4)
Amp1_B1 = Dados_wad (:,10);
subplot(3,1,1)
plot(Amp1_B1)
title ('Amplitude (Beam1)')

Amp2_B2= Dados_wad (:,11);
subplot(3,1,2)
plot(Amp2_B2)
title ('Amplitude (Beam2) ')

Amp3_B3= Dados_wad (:,12);
subplot(3,1,3)
plot(Amp3_B3)
title (' Amplitude (Beam3)')

%%
% ARQUIVO.v1
%  1   Velocity Cell 1 (Beam1|X|East)   (m/s)
%  2   Velocity Cell 2 (Beam1|X|East)   (m/s)
%      .
%      .
%  n   Velocity Cell n (Beam1|X|East)   (m/s)
% 
% ---------------------------------------------------------------------
% ARQUIVO.v2
%  1   Velocity Cell 1 (Beam2|Y|North)  (m/s)
%  2   Velocity Cell 2 (Beam2|Y|North)  (m/s)
%      .
%      .
%  n   Velocity Cell n (Beam2|Y|North)  (m/s)
% 
% ---------------------------------------------------------------------
% ARQUIVO.v3
%  1   Velocity Cell 1 (Beam3|Z|Up)     (m/s)
%  2   Velocity Cell 2 (Beam3|Z|Up)     (m/s)
%      .
%      .
%  n   Velocity Cell n (Beam3|Z|Up)     (m/s)


%V1 camada 1 = *ONDAS (compara)
load ('ADCP_05_08_2015v1.v1')
Dados_v1 = ADCP_05_08_2015v1;
v1c1=Dados_v1(:,1);        % V1 camda 1 East
Med_v1c1= mean(v1c1);          % M�dia de V1
v1c1M=v1c1-mean(v1c1);         % tirando a M�dia de V1
Medv1c1=v1c1-Med_v1c1;         % a m�dia ponto a ponto da serie

%V1 camada 2
v1c2=Dados_v1(:,2);           % V1 camada 2 East
Med_v1c2= mean(v1c2);          % M�dia de V1
v1c2M=v1c2-mean(v1c2);         % tirando a M�dia de V1
Medv1c2=v1c2-Med_v1c2;

%V1 camada 3
v1c3=Dados_v1(:,3);           % V1 camada 3 East
Med_v1c3= mean(v1c3);        % M�dia de V1
v1c3M=v1c3-mean(v1c3);         % tirando a M�dia de V1
Medv1c3=v1c3-Med_v1c3;

load ('ADCP_05_08_2015v2.v2')
%V2 camada 1
Dados_v2 = ADCP_05_08_2015v2;
v2c1=Dados_v2(:,1);           % V2 North
Med_v2c1= mean(v2c1);          % M�dia de V1
v2c1M=v2c1-mean(v2c1);         % tirando a M�dia de V2
Medv2c1=v2c1-Med_v2c1;         % a m�dia ponto a ponto da serie

%V2 camada 2
v2c2=Dados_v2(:,2);           % V1 camada 2 North
Med_v2c2= mean(v2c2);          % M�dia de V1
v2c2M=v2c2-mean(v2c2);         % tirando a M�dia de V2
Medv2c2=v2c2-Med_v2c2;         % a m�dia ponto a ponto da serie

%V2 camada 3
v2c3=Dados_v2(:,3);           % V2 camada 3 North
Med_v2c3= mean(v2c3);        % M�dia de V2
v2c3M=v2c3-mean(v2c3);         % tirando a M�dia de V2
Medv2c3=v2c3-Med_v2c3;         % a m�dia ponto a ponto da serie

load ('ADCP_05_08_2015v3.v3')
%V3 camada 1
Dados_v3 = ADCP_05_08_2015v3;
v3c1=Dados_v3(:,1);           %  V3 Up Z
Med_v3c1= mean(v3c1);          % M�dia de V3
v3c1M=v3c1-mean(v3c1);         % tirando a M�dia de V3

%V3 camada 2
v3c2=Dados_v3(:,2);           % V3 camada 2 UP
Med_v3c2= mean(v3c2);          % M�dia de V1
v3c2M=v3c2-mean(v3c2);         % tirando a M�dia de V2
%V3 camada 3
v3c3=Dados_v3(:,3);           % V3 camada 3 UP
Med_v3c3= mean(v3c3);        % M�dia de V2
v3c3M=v3c3-mean(v3c3);         % tirando a M�dia de V2


% V1 x V2 x V3 x mare 
figure(5)                 
subplot(5,1,1)
plot(v1c1,'r')
hold on
plot(v2c1,'g')
plot(v3c1,'b')
plot([0 46],[0 0],'k','LineWidth',1)
xlabel('tempo')
ylabel('Velocidade (m/s)')
legend('East', 'North','Up')
axis([0 47 -0.5 0.5]);
title('C1')

subplot(5,1,2)
plot(v1c2,'r')
hold on
plot(v2c2,'g')
plot(v3c2,'b')
plot([0 46],[0 0],'k','LineWidth',1)
xlabel('tempo')
ylabel('Velocidade (m/s)')
legend('East', 'North','Up')
axis([0 47 -0.7 0.7]);
title('C2')

subplot(5,1,3)
plot(v1c3,'r')
hold on
plot(v2c3,'g')
plot(v3c3,'b')
plot([0 46],[0 0],'k','LineWidth',1)
xlabel('tempo')
ylabel('Velocidade (m/s)')
legend('East', 'North','Up')
axis([0 47 -0.7 0.7]);
title('C3')

%Vetor - Corrente Resultante
[dir1,spd1] = uv2polar(v1c1,v2c1);
Vdir1 = dir1-4-22.38;
subplot (5,1,4)
plot(Vdir1,'k.-');
axis([0 47 0 360]);
ylabel('Dire��o')
title('Resultante direcional')

subplot(5,1,5)
plot(Press_Sen-mean(Press_Sen))
axis([0 47 -0.8 0.8]);
xlabel('tempo')
ylabel('Amplitude (m)')


%% sinal
% ARQUIVO.a1
%  1   Amplitude Cell 1 (Beam1)         (counts)
%  2   Amplitude Cell 2 (Beam1)         (counts)
%      .
%      .
%  n   Amplitude Cell n (Beam1)         (counts)
% 
% ---------------------------------------------------------------------
% ARQUIVO.a2
%  1   Amplitude Cell 1 (Beam2)         (counts)
%  2   Amplitude Cell 2 (Beam2)         (counts)
%      .
%      .
%  n   Amplitude Cell n (Beam2)         (counts)
% 
% ---------------------------------------------------------------------
% ARQUIVO.a3
%  1   Amplitude Cell 1 (Beam3)         (counts)
%  2   Amplitude Cell 2 (Beam3)         (counts)
%      .
%      .
%  n   Amplitude Cell n (Beam3)         (counts)

% a1 a2 a3

load ('ADCP_05_08_2015a1.a1');
Dados_amp1 = ADCP_05_08_2015a1;
a1a1 = Dados_amp1 (:,1);
a1a2 = Dados_amp1 (:,2);
a1a3 = Dados_amp1 (:,3);

load ('ADCP_05_08_2015a2.a2');
Dados_amp2 = ADCP_05_08_2015a2;
a2a1 = Dados_amp2 (:,1);
a2a2 = Dados_amp2 (:,2);
a2a3 = Dados_amp2 (:,3);

load ('ADCP_05_08_2015a3.a3');
Dados_amp3 = ADCP_05_08_2015a3;
a3a1 = Dados_amp3 (:,1);
a3a2 = Dados_amp3 (:,2);
a3a3 = Dados_amp3 (:,3);

figure(6)                 
subplot(3,1,1)
plot(a1a1,'r')
hold on
plot(a1a2,'g')
plot(a1a3,'b')
legend('a1a1', 'a1a2','a1a3')
title('Amplitude Cell 1 (Beam1) - Arquivo.a1')

subplot(3,1,2)
plot(a2a1,'r')
hold on
plot(a2a2,'g')
plot(a2a3,'b')
legend('a2a1', 'a2a2','a2a3')
title('Amplitude Cell 1 (Beam2) - Arquivo.a2')

subplot(3,1,3)
plot(a3a1,'r')
hold on
plot(a3a2,'g')
plot(a3a3,'b')
legend('a3a1', 'a3a2','a3a3')
title('Amplitude Cell 1 (Beam3) - Arquivo.a3')


figure(7)
subplot(3,1,1)
plot(PressWad-mean(PressWad))
title ('Mar� e Ondas (Press�o.wad)')
subplot(3,1,2)
plot(Press_Sen-mean(Press_Sen))
title('Mar� (Press�o.sen)') 
H=PressWad-mean(PressWad) %tirando a m�dia
%H= pressao-mean (pressao); %n eleva�l�o da Sup do Mar 
mare=smooth(H,2000); %tiro a mar�
Onda=H-mare;    %tiro a mar� do nivel
subplot(3,1,3)
plot(Onda)
title ('Ondas')


%% DADOS v�lidos .dat
%% ROTINA para Observar a MAGNITUDE das COrrentes do Aquadopp
% modificado de prof Francisco - URUGUAI
%
set(0,'DefaultAxesFontSize',14);  % para que o tamanho das fontes sejam 14

% ARQUIVO.DAT
filenamecurrents='ADCP_05_08_2015.dat';

[E,V]=currentdataread(filenamecurrents);
t=[5:42];

%% CALCULO DA CORRENTE
zcorr=0; %denomimando a primeira celula (fora da �gua - ajustavel)

ve= squeeze(V(:,3,:));  % matriz com as componentes X Leste m/s
vn= squeeze(V(:,4,:));  % matriz com as componentes Y Norte m/s
vm= squeeze(V(:,9,:));  % modulo
z= squeeze(V(:,2,:));   % posi��o da c�lula
p= E(:,14)';            % prof agua (sensor de press�o)
[c,h]=size(z);            % c - numero de celulas/ h  - horas
pz=repmat(p,c,1)-zcorr;   %tirando a primeira celula
dir= squeeze(V(:,10,:));

% v = ve + vn*1i; %representacao quadrada complexa
% vm = abs(v); % modulo da velocidade

c_val=boolean(z<pz); %celulas v�lidas - celulas dentro da �gua 
                     % de acordo com o sensor de press�o
z_val=z*NaN;         % celulas que est�o fora ter�o valor de NaN
z_val(c_val)=z(c_val); % posi��o das celulas validas

ve_val=ve*NaN;          %  posi��o das celulas leste validas
ve_val(c_val)=ve(c_val);% velocidade leste -  celulas v�lidas

vn_val=vn*NaN;           %  posi��o das celulas norte validas
vn_val(c_val)=vn(c_val); % velocidade norte -  celulas v�lidas

vm_val=vm*NaN;           %  posi��o das celulas modulo da vel validas
vm_val(c_val)=vm(c_val); % velocidade modulo da vel -  celulas v�lidas

cs=sum(c_val);           % celulas superficial de acordo com a press�o
zcs=max(z_val);

vecs=cs*NaN; % valores da velocidade superficial leste de acordo com o sensor de press�o
vncs=cs*NaN; % valores da velocidade superficial norte de acordo com o sensor de press�o
vmcs=cs*NaN; % valores do modulo da velocidade superficial de acordo com o sensor de press�o

for i=1:h
    if cs(i)~=0
        vecs(i)=ve_val(cs(i),i);
        vncs(i)=vn_val(cs(i),i);
        vmcs(i)=vm_val(cs(i),i);
    end
end

% inverter esse gr�fico no editor
figure(8)
set(0,'DefaultAxesFontSize',14);  
imagesc(5:42,(V(:,2,1)),(vm_val(1:5,5:42)))
hold on
plot(t,E(5:42,14),'k','linewidth',2)
title('Magnitude das Correntes: 21 e 22/Nov/2015')
legend('Mar�')
ylabel('Profundidade (m)')
xlabel ('Medidas (burst)')

figure(9)
plot(vecs(1,3:42),'r')
ylabel('Velocidade m/s')
hold on
plot(vncs (1,3:42),'b')
hold on
plot(E(:,14),'k')
axis([0 42 -1 3])
legend('Vel Vx','Vel Vy','Mar�')
plot([0 42],[0 0],'k-.','LineWidth',1)
xlabel('Escala Temporal')

%% ONDAS

dt=0.5 ;
eta = Onda;
t=(linspace(dt,length(eta)*dt,length(eta)))';
h = 3.5; %profundidade
%chama subrotina de processamento de onda no dominio do tempo (Tza, Hs..)
[Hs,H10,Hmed,Hmin,Hmax,Tmed,Tmin,Tmax,THmax,Lmed,Lmax,Lmin,Cmed]=onda_tempo(t,eta,h);

pfadcp = 0;

pathname = ('ADCP_05_08_2015.wad');

%pathname_adv = ('C:\Users\douglas.MENTAWAII\Documents\18 05-08\ADV');

dd = load(pathname);
    
%ADCP
%cada burst tem 2048 pontos em 2 Hz (dt = 0.5)

% ??? tem que dar uma olhada aqui, pq a programa��o do instrumento vai
% determinar o comprimento (1024).... ??? 
c = 0;
for i = 1:1024:length(dd)
    
    c = c + 1;
    pr(:,c) = dd(i:i+1024,3);
    vx(:,c) = dd(i:i+1024,6);
    vy(:,c) = dd(i:i+1024,7);
    vz(:,c) = dd(i:i+1024,8);
    
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

    Dir (:,c) = diraz - 22.5
    figure(10)
    subplot(2,1,1,'fontsize',14)
    plot(f,an,'-*');hold on
    axis([0 0.4 0 0.3])
    title('ADCP - vz')
    xlabel('Frequencia');ylabel('Energia')
    title('Espectro de Frequ�ncias')
    grid on;
    
    subplot(2,1,2)
    plot(f,Dir,'-*');hold on
    ylim([0,360])
    xlim([0,0.4])
    xlabel('Frequencia');ylabel('Dire��o')
    title('Espectro Direcional')
    grid on;
    

end
