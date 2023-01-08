package salasystem;

import personagem.Personagem;

public class Porta implements Interactable {
    private Sala salaA;
    private Sala salaB;
    private boolean open = true;
    private Item chave;

    public Porta(Sala a, Sala b) {
        this.salaA = a;
        this.salaB = b;
    }

    public Sala getOtherSide(Sala sala_atual) {
        if (sala_atual == salaA)
            return salaB;
        return salaA;
    }

    public boolean isOpen() {
        return this.open;
    }

    private void open(CanInteract autor) {
        if (condition(autor))
            this.open = true;
            onOpenEvent(autor);
    }

    private void close(CanInteract autor) {
        this.open = false;
    }

    protected boolean condition(CanInteract autor) {
        if (autor instanceof Personagem) {
            if (autor.hasItem(getChave()))
                return true;
            return false;
        }
        return true;
    }

    protected void onOpenEvent(CanInteract autor) {}

    @Override
    public void interact(CanInteract autor) {
        interactionEvent(autor);
        if (isOpen())
            close(autor);
        else
            open(autor);

    }

    protected void interactionEvent(CanInteract autor) {}

    public Item getChave() throws NullPointerException {
        return this.chave;
    }
}
