%Calculo do 'a' e 'b' da Regressão linear
function [b,a]=regressao(x,y)



%Exemplo: x=[139.88 ; 139.92];
%         y=[-3.99 ; 11.87];

n=length(x);    %comprimento da matriz x --> 2
xy=x.*y;        %multiplica a matriz x*y
somaxy=sum(xy); %somatório de x*y
somax=sum(x);   %somatório de x
somay=sum(y);   %somatório de y
medxy=mean(xy); %média de x*y
somax2=sum(x.^2);   %somatório de (x^2)
medx2=(mean(x).^2); %média de x^2 --> (media de x)^2
somaxquad=somax^2;  %(somatório de x)^2

b=(somax2*somay-somaxy*somax)/(n*somax2-somaxquad);
a=(n*somaxy-somax*somay)/(n*somax2-somaxquad);

