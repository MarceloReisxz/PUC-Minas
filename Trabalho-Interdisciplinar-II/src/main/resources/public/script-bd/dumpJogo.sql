SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: id-jogo; Type: SEQUENCE; Schema: public; Owner: 
--

CREATE SEQUENCE public."id-jogo"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 1000000
    CACHE 1;


ALTER TABLE public."id-jogo" OWNER TO x;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: jogo; Type: TABLE; Schema: public; Owner: 
--

CREATE TABLE public.jogo (
    id integer DEFAULT nextval('public."id-jogo"'::regclass) NOT NULL,
    nome text,
    preco double precision
);


ALTER TABLE public.jogo OWNER TO x;

--
-- Name: jogo jogo_pkey; Type: CONSTRAINT; Schema: public; Owner: 
--

ALTER TABLE ONLY public.jogo
    ADD CONSTRAINT jogo_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--   

