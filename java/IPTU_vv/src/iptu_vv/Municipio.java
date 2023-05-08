package iptu_vv;

import java.util.ArrayList;
import java.util.List;

/**
 * Classe para objetos do tipo Município, onde serão contidos valores e métodos para o mesmo
 */
public class Municipio {
    List<Imovel> imoveis = new ArrayList<>();
    
    public Municipio(){
        
    }
    /** Método que busca um objeto do tipo Imóvel em uma lista contida no objeto Município*/
    void AdicionarImovel(Imovel i){
        imoveis.add(i);
    }
    
    /** Método que exibe atributos de objetos do tipo Imóvel contidos no objeto Município*/
    void exibirImoveis(){
        for (Imovel i: imoveis){
            System.out.print("\nNome do proprietario: "+ i.nome +" | ");
            System.out.print("Meses de atraso: "+ i.meses_atraso + " | ");
            System.out.print("Valor do imovel: "+ i.valor + "\n");
        }
        
    }
    /** Método que pesquisa a multa de um objeto do tipo Imóvel pelo nome da pessoa a quem o imóvel pertence 
     * @param nome
     * @return double - valor da multa*/
    double pesquisarMultaPorNome(String nome){
        for (Imovel i: imoveis){
            if (i.nome.equals(nome)){
                double m = i.valorMulta();
                System.out.println("\nA multa dessa pessoa é de "+ m +" reais");
                return m;
            }
        }
        System.out.println("\nEssa pessoa não tem um imovel nessa cidade");
        return 0;
    }
}
