% Calcula o espectro cruzado entre duas series reais
% utilizando a funcao 'spectrum'
%
% Elaborado por Henrique P. P. Pereira (henriqueppp@peno.coppe.ufrj.br)
%
% Ultima modificacao: 01/11/2012
%
% Dados de entrada: x - serie real (ex: elevacao do mar)
%                   y - serie real (ex: elevacao do mar)
%                   dt - intervalo amostragem
%                   gl - graus de liberdade (padrao: 32)
%  
% Dados de saida: matriz ss2: - col 1 - vetor de frequencia
%                               col 2 - autoespectro de x
%                               col 3 - autoespectro de y
%                               col 4 - co-espectro
%                               col 5 - quad-espectro
%                               col 6 - ampl. espec.cruz xy 
%                               col 7 - espectro de fase xy
%                               col 8 - coerencia
%                               col 9 - funcao de transferencia
%                               col 10 - int. confianca x ??
%                               col 11 - int. confianca y ??
%                               col 12 - int. confianca coerencia ??

function [ss2]=spec2(x,y,dt,gl)


%seleciona 1024 registros da serie (pode variar desde que com mesmo comprimento)
x=x(1:1024);
y=y(1:1024);

%graus de liberdade (ex: 2, 4, 8, 32..) - alisa o espectro
% gl=2;

%comprimento do registro
reg=length(x);

%comprimento do vetor do espectro
N=reg/(gl/2);

%frequencia de nysquit (frequencia de corte)
fny=1/(2*dt);

%vetor de frequencia
% f=(fny/reg:(gl*fny)/reg:fny)'; %errado
f=(1/(N*dt):1/(N*dt):fny)';

%numero de subdivisoes para o calculo do espectro
subd=reg/(gl/2);

%overlaping de 50% para o calculo do espectro
ov=subd/2;

%chama subrotina spectrum (com x e y calcula o espectro cruzado)
sp2=spectrum(x,y,subd,ov,'welch');

%separa componente real e imaginaria (cria 2 matrizes)
sp2re=real(sp2);
sp2im=imag(sp2);

% Correções necessarias para a funcao fft e spectrum (perguntar para o parente)
% fft: - nao divide por N
%      - nao multiplica por dt 
% spectrum: - divide por N
%           - nao multiplica por dt
% multiplica por 2, por que?? fator de escala?

%multipilca por 2*dt os autoespectros de x e y
sp2re(:,1:2)=2*dt*sp2re(:,1:2);

%autoespectro de x (retira a linha 1 que e a media)
aspx=sp2(2:length(sp2),1);

%autoespectro de y (retira a linha 1 que e a media)
aspy=sp2(2:length(sp2),2);

%amplitude do espectro cruzado de x y (perguntar para o parente se
%multiplica o real com o imaginario, e se mutlipilca por 2*dt )
% spxy=sp2re(2:length(sp2re),3);
spxy=sqrt(sp2im(2:length(sp2im),3).^2+sp2re(2:length(sp2re),3).^2); %feito da espec2 do JL

%exemplo joao: ampln1n2 = sqrt(qdn1n2.^2+con1n2.^2); %Joao luiz

%calculo do co-espectro e quad-espectro (perguntar parao parente, se é para
%pegar as partes reais (co) e imaginarias (quad) dos valores brutos do espectro cruzado de x e y 
cosp=sp2re(2:length(sp2re),3);
qdsp=sp2im(2:length(sp2im),3);

%espectro de fase (rotina espec2 JL)
fasexy=atan(qdsp./cosp)*180/pi;

%ex: fasen1n2 = atan(qdn1n2./con1n2)*180/pi;

%obs: fazer o teste da maneira da noaa, paper nondirection and direction wave...

%funcao de transferencia (perguntar mais sobre para o parente)
ftr=sp2re(2:length(sp2re),4);

%funcao de coerencia
fco=sp2re(2:length(sp2re),5);

%intervalo de confiaca de x -- verificar!!!
icx=sp2re(2:length(sp2re),6);

%intervalo de confiaca de y -- verificar!!!
icy=sp2re(2:length(sp2re),7);

%intervalo de confiaca da funcao de coerencia -- verificar!!!
icco=sp2re(2:length(sp2re),8);

[ss2]=[f aspx aspy cosp qdsp spxy fasexy fco ftr icx icy icco];





