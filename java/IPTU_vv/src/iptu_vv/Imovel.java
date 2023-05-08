package iptu_vv;
/** 
 * Classe para objetos do tipo Imóvel, onde serão contidos valores e métodos para o mesmo
 */
public class Imovel {
    String nome;
    double imposto;
    int meses_atraso;
    float valor;
    Municipio cidade;

    /**
     *
     * @param nome
     * @param meses_atraso
     * @param valor
     */
    public Imovel(String nome, int meses_atraso, float valor) {
        this.nome = nome;
        this.meses_atraso = meses_atraso;
        this.valor = valor;
        this.imposto = this.definirImposto(meses_atraso);
    }
    
    /**
     *
     */
    public Imovel(){
        
    }
    /** 
     * Método que atribui o nome do dono do imóvel para o objeto
     */
    void definirNome(String nome){
        this.nome = nome;
    }
    /** Método que atibui quando meses o imóvel está atrasado
     * @param meses 
     */ 
    void definirMesesAtraso(int meses){
        this.meses_atraso = meses;
        this.definirImposto(this.meses_atraso);
    }
    /** Método que atribui o valor do imóvel
     * @param valor
     */
    void definirValor(float valor){
        this.valor = valor;
    }
    
    /** Método que defini o valor do imposto refente a quantidade de meses atrasados
     * 
     * @param meses 
     */
    double definirImposto(int meses){
        if (meses <= 5){
            return 0.01;
        }
        if (meses > 5 && meses <= 8){
            return 0.023;
        }
        if (meses > 8 && meses <= 10){
            return 0.03;
        }
        if (meses > 10 && meses <= 12){
            return 0.054;
        }
        if (meses > 12){
            return 0.1;
        }
        return 0;
    }
    
    /** Método que calcula o valor da multa do imóvel
     * 
     * @return double - valor multa
     */
    double valorMulta(){
        //double multa = 1*(Math.pow((1+this.imposto), this.meses_atraso)) - 1;
        double multa = this.valor * this.imposto * this.meses_atraso;
        return multa;
    }
}
